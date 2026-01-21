from pymongo import MongoClient


class Verify:
    def __init__(self):
        self.uri = "mongodb+srv://projectssayo_db_user:gEgSg9ug08WTP6NA@cluster0.pd254jn.mongodb.net/?appName=Cluster0"
        self.client = MongoClient(self.uri)
        self.db = self.client["suyognegi1_projects_sayo"]
        self.users = self.db["admin_pass"]

    def verify_password_one_input(self, password: str) -> dict:

        passwo = self.users.find_one({"_id": password})

        if not passwo:
            return {"found": False, "valid_password": False}
        return {"found": True, "valid_password": True}
