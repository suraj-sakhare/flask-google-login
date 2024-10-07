from flask import Flask, render_template
from routes.auth import auth_bp
from routes.protected import protected_bp
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Registering Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(protected_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
