# Overengineered Flask example

A small but over-engineered Flask project, showcasing the following:

1. Custom error handlers for 404 Not Found and 403 Not Authorized pages
2. Decorator for authorization checking (`@authorize`)
3. Decorator for JSON vs HTML server reply (`@reply`)
4. A trick for preventing default 404 on the favicon (this requires a PNG to actually exists in the `/static/` folder)
5. Blueprints, because separation of concerns rules!

## To install:

1. Make sure you have at least Python 3. installed
2. Download the project as a zip, or `git clone` it
3. Create a virtual environment in the project folder: `python3 -m virtualenv venv`
   1. If virtualenv is not found, install it: `pip3 install virtualenv`
   2. Then create it
4. Activate the virtualenv:
   1. Linux/Mac: `source venv/bin/activate`
   2. Windows: `./venv/Scripts/Activate.ps1`
5. Install dependencies: `pip3 install -r requirements.txt`
6. Run the server: `python3 server.py`

Feel free to look around the files, see what does what. Be aware, it's not connected in any way to a database. **This is just an example.**

Have fun!