import os
from server import app, oauth
from models.user import User
from dotenv import load_dotenv
from flask import redirect, session,  url_for
from urllib.parse import quote_plus, urlencode

load_dotenv()

@app.route("/")
def home():
	return redirect("/")

@app.route("/callback", methods=["GET", "POST"])
def callback():
	token = oauth.auth0.authorize_access_token()
	user_info = oauth.auth0.parse_id_token(token)
	user = User(user_info)
	user.save_to_mongo()
	session["user"] = token
	return redirect("/")

@app.route("/login")
def login():
	return oauth.auth0.authorize_redirect(
		redirect_uri=url_for("callback", _external=True)
	)

@app.route("/logout")
def logout():
	session.clear()
	return redirect(
		"https://"
		+ os.getenv("AUTH0_DOMAIN")
		+ "/v2/logout?"
		+ urlencode(
			{
				"returnTo": url_for("home", _external=True),
				"client_id": os.getenv("AUTH0_CLIENT_ID"),
			},
			quote_via=quote_plus
		)
	)