from server import app
from pymongo.errors import DuplicateKeyError

class User:
	def __init__(self, user_info):
		self.user_info = user_info
	
	def save_to_mongo(self):
		collection = app.db.users
		existing_user = collection.find_one({"auth0_id": self.user_info["sub"]})

		if existing_user is None:
			try:
				collection.insert_one({
					"auth0_id": self.user_info["sub"],
					"email": self.user_info["email"],
					"name": self.user_info["name"],
					"created_at": self.user_info.get("created_at", None),
				})
			except DuplicateKeyError:
				pass