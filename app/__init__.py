from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine


app=Flask(__name__)
upload_folder='app\static\media'
api=Api(app)
DB_URI='mongodb://localhost:27017/assignment'
app.config["MONGODB_HOST"]=DB_URI
app.config["UPLOAD_FOLDER"]=upload_folder
db=MongoEngine()
db.init_app(app)

from app import routes