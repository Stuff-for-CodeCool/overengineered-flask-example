"""Provides Reply and Authorize decorators, as well as text processing functions"""
from flask import jsonify, request, render_template, session, url_for
from werkzeug.exceptions import Forbidden


def reply(function):
    """Replies with JSON for JSON requests, template otherwise"""

    def wrapper(*args, **kwargs):  # decorators always return a function
        # Server functions MUST return a (template, data) tuple
        template, data = function(*args, **kwargs)

        if request.is_json:  # checks for JSON request
            return jsonify(data)  # replies with JSON

        return render_template(template, **data)  # not JSON, output template

    wrapper.__name__ = function.__name__  # this prevents an AssertionError

    return wrapper


def authorize(function):
    """Checks for key "user" in session; Continues if present, raises Forbidden otherwise"""

    def wrapper(*args, **kwargs):

        if not session.get("user", None):
            raise Forbidden

        # returns the function as-is; used BEFORE @reply defined above
        return function(*args, **kwargs)

    wrapper.__name__ = function.__name__
    return wrapper


def wrap(text, tag="p"):
    """Given a long string, wraps lines with specified tag"""
    lines = [line.strip() for line in text.split("\n") if len(line.strip())]
    return "\n".join(
        f"<{tag}>{line}</{tag}>" if not line.startswith("<") else line for line in lines
    )


def link_scripts(scripts, folder="static"):
    """Given an array of strings, will create proper script tags"""
    urls = [url_for(folder, filename=script) for script in scripts]
    return "\n".join(f'<script src="{url}" defer></script>' for url in urls)
