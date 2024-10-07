import os
import requests
from flask import Blueprint, session, redirect, request, abort
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
import google.auth.transport.requests
from pip._vendor import cachecontrol
from config import Config

auth_bp = Blueprint('auth_bp', __name__)

# Initialize OAuth flow
flow = Flow.from_client_secrets_file(
    client_secrets_file=Config.CLIENT_SECRETS_FILE,
    scopes=Config.SCOPES,
    redirect_uri=Config.REDIRECT_URI
)

@auth_bp.route("/login")
def login():
    """Initiates the OAuth flow."""
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@auth_bp.route("/callback")
def callback():
    """Handles the callback from Google after user authentication."""
    flow.fetch_token(authorization_response=request.url)

    if session["state"] != request.args["state"]:
        abort(500)  # State mismatch

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=Config.GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")

@auth_bp.route("/logout")
def logout():
    """Logs the user out and clears the session."""
    session.clear()
    return redirect("/")
