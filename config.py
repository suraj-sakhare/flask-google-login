import os
import pathlib

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "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"  # Use a strong secret key
    GOOGLE_CLIENT_ID = "68960912092-umbpqi2mjiao4c5mcvt2kh710b3q229k.apps.googleusercontent.com"  # Replace with your Google client ID
    CLIENT_SECRETS_FILE = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
    OAUTHLIB_INSECURE_TRANSPORT = os.environ.get("OAUTHLIB_INSECURE_TRANSPORT", "1")  # Allow HTTP traffic for local dev
    SCOPES = ["https://www.googleapis.com/auth/userinfo.profile",
              "https://www.googleapis.com/auth/userinfo.email", "openid"]
    REDIRECT_URI = "http://127.0.0.1:5000/callback"
