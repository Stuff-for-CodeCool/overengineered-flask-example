"""Module handling private pages"""
from flask import Blueprint, url_for, session, request
from werkzeug.utils import redirect
from utils import authorize, reply, wrap, link_scripts

private = Blueprint(
    name="private",  # blueprint's name is the folder name; __name__ will NOT work
    import_name="private",  # both name and import_name have to be set
    static_folder="./blueprints/private/static",  # notice the "./" before the name
    url_prefix="/private",  # the path for the current folder
)

# Notice @authorize before @reply
# @reply expects ALL view functions to return a tuple
# This will be ("template_to_be_shown.html", dict_of_key-value_pairs_with_data)
@private.get("/")
@authorize
@reply
def index():
    """Default private page"""

    message = f"""
    This is some private content

    <a href="{ url_for('private.another') }">Look at another private page</a>
    """

    data = {
        "title": "Private pages",
        "message": wrap(message),
    }

    return ("index.html", data)


@private.get("/login")
@private.get("/login/")
@reply
def login():
    """Login page"""

    message = f"""
    <form action="{ url_for('private.login_handler') }" method="post">
        <label for="username">Username</label>
        <input id="username" name="username" type="text" />
        <label for="password">Password</label>
        <input id="password" name="password" type="password" />
        <button type="submit">Login</button>
    </form>
    """

    data = {
        "title": "Login",
        "message": wrap(message),
        "scripts": link_scripts(
            [
                "js/login_form.js",
                "js/public_nav.js",
            ]
        ),
    }

    return ("index.html", data)


@private.post("/login")
@private.post("/login/")
def login_handler():
    """Fakes login, does not actually work"""

    # Takes field valuess from JSON if it's a JSON request
    # Otherwise takes them from the form
    user = request.json["username"] if request.is_json else request.form["username"]
    pssd = request.json["password"] if request.is_json else request.form["password"]

    print(f"\nGot username '{user}' with password '{pssd}'\n")

    session["user"] = user
    return redirect(url_for("private.index"))


@private.get("/logout")
@private.get("/logut/")
def logout():
    """Logs out user"""
    session.clear()
    return redirect(url_for("index"))


# # Several routes all link to the same function
@private.get("/another")
@private.get("/another/")
@private.get("/another/<int:page>")
@private.get("/another/<int:page>/")
@reply
def another(page=1):
    """Example private page, showcasing navigation"""

    current_page = max(1, min(page, 4))
    prev_page = (
        url_for("private.another", page=current_page - 1) if current_page > 1 else None
    )
    next_page = (
        url_for("private.another", page=current_page + 1) if current_page < 4 else None
    )

    message = f"""
    <h1>This is page {current_page}</h1>
    There's a simple trick to limit the number of extra pages.
    Check <code>blueprints/private/__init__.py</code> for details.

    <nav>
    { f'<a href="{prev_page}">Previous page</a>' if prev_page else "" }
    { f'<a href="{next_page}">Next page</a>' if next_page else "" }
    </nav>

    """
    data = {
        "title": "Private pages",
        "message": wrap(message),
        "scripts": link_scripts(["js/public_nav.js"]),
    }
    return ("index.html", data)
