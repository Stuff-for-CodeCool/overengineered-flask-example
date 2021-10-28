"""Module handling all public pages"""
# A file named __init__.py in a folder allows the whole folder to be imported as a module

from flask import Blueprint, url_for
from app.utils import reply, wrap, link_scripts

public = Blueprint(
    name="public",  # blueprint's name is the folder name; __name__ will NOT work
    import_name="public",  # both name and import_name have to be set
    template_folder="./app/blueprints/public/templates",  # notice the "./" before the name
    url_prefix="/public",  # the path for the current folder
)

# Starting with Flask 2.0.0, routes can be HTML verbs
@public.get("/")
@reply
def index():
    """Default public page"""

    message = f"""
    <h1>Hello</h1>
    This is a lot of content.
    It will be wrapped in paragraphs, and will be available for everyone.
    <a href="{ url_for('public.another') }">Look at another public page</a>
    """

    data = {
        "title": "Public pages",
        "message": wrap(message),
    }

    return ("index.html", data)


# Several routes all link to the same function
@public.get("/another")
@public.get("/another/")
@public.get("/another/<int:page>")
@public.get("/another/<int:page>/")
@reply
def another(page=1):
    """Example public page, showcasing navigation"""

    current_page = max(1, min(page, 4))
    prev_page = (
        url_for("public.another", page=current_page - 1)
        if current_page > 1
        else None
    )
    next_page = (
        url_for("public.another", page=current_page + 1)
        if current_page < 4
        else None
    )

    message = f"""
    <h1>This is page {current_page}</h1>
    There's a simple trick to limit the number of extra pages.
    Check <code>blueprints/public/__init__.py</code> for details.
    
    <nav>
    { f'<a href="{prev_page}">Previous page</a>' if prev_page else "" }
    { f'<a href="{next_page}">Next page</a>' if next_page else "" }
    </nav>
    
    """
    data = {
        "title": "Public pages",
        "message": wrap(message),
        "scripts": link_scripts(["js/public_nav.js"]),
    }
    return ("index.html", data)
