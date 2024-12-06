import os
from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from authlib.integrations.flask_client import OAuth

load_dotenv()
secret_key = os.getenv("SECRET_KEY")
mongo_uri = os.getenv("MONGO_URI")

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
app.config["MONGO_URI"] = mongo_uri

mongodb_client = PyMongo(app)
db = mongodb_client.cx["lushly"]

oauth = OAuth(app)

oauth.register(
	"auth0",
	client_id=os.getenv("AUTH0_CLIENT_ID"),
	client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
	client_kwargs={
		"scope": "openid profile email",
	},
	server_metadata_url=f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)

# Testing
print(f"mongodb_client: {mongodb_client}")
print(f"db: {db}")


from routes import user