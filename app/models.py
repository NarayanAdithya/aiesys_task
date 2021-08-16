from app import db
from flask_bcrypt import generate_password_hash, check_password_hash
class User(db.Document):
    userID = db.UUIDField(required=True,binary=False)
    name=db.StringField(required=True)
    username=db.StringField(required=True)
    password=db.StringField(required=True,min_length=6)
    scope=db.StringField(required=True)
    profile_pic=db.StringField(required=True)
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self,password):
        return check_password_hash(self.password,password)
    
class item(db.Document):
    itemID=db.UUIDField(required=True,binary=False)
    itemname=db.StringField(required=True)
    sellingprice=db.IntField(required=True)
    costprice=db.IntField(required=True)
    offer=db.IntField(required=True)
