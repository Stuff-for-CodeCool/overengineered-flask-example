"""The example server, with everything nicely documented"""
#   general imports
from os import getenv, path
from dotenv import load_dotenv

#   Flask imports
from flask import Flask, url_for, redirect, session, send_from_directory
from utils import reply

#   import blueprints
from blueprints.public import public
from blueprints.private import private

load_dotenv()  # load environment variables

app = Flask(__name__)  # declare application
app.secret_key = getenv("SECRET_KEY")  # set secret key, needed for session

#   Register blueprints
app.register_blueprint(public)
app.register_blueprint(private)

# App entry point
@app.route("/")
def index():
    """Redirects to public page by default"""
    return redirect(url_for("public.index"))


#   Page Not Found handler
@app.errorhandler(404)
@reply
def not_found(_):
    """404 handler"""
    return (
        "error_page.html",
        {"message": "Page not found", "error": 404},
    )


#   Page Not Authorized handler
@app.errorhandler(403)
def not_authorized(_):
    """403 handler redirecting to login page"""
    return redirect(url_for("private.login"))


@app.route("/favicon.ico")
def favicon():
    """Stupid trick to remove 404 for favicon"""
    return send_from_directory(
        path.join(app.root_path, "static"),
        "favicon.png",
        mimetype="image/vnd.microsoft.icon",
    )


#   Run application
if __name__ == "__main__":
    app.run(debug=True)
