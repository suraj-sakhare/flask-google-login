from flask import Blueprint, session, abort, render_template

protected_bp = Blueprint('protected_bp', __name__)

def login_is_required(function):
    """Decorator to require login for protected routes."""
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function(*args, **kwargs)

    return wrapper

@protected_bp.route("/protected_area")
@login_is_required
def protected_area():
    """Protected area accessible only to logged-in users."""
    return render_template("protected_area.html", name=session['name'])
