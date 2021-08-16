from werkzeug.utils import secure_filename
from flask_restful import Resource
from flask import request,jsonify,make_response
from app.models import User,item
from app import app
import uuid
import os
class signup(Resource):
    def post(self):
        body=request.form
        f=request.files['profilepic']
        print(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        u=User(userID=uuid.uuid4(),
        name=body['name'],
        username=body['username'],
        password=body['password'],
        scope=body['scope'],
        profile_pic=secure_filename(f.filename)
        )
        u.hash_password()
        u.save()
        return make_response(jsonify({'succees':True}))
        

class signin(Resource):
    def post(self):
        body=request.get_json()
        u=User.objects.get(username=body['username'])
        if(u.check_password(body['password'])):
            if(u['scope']=='admin'):
                return make_response(jsonify({"Access":"Admin Previlages",'User':u,'success':True}))
            else:
                return make_response(jsonify({"Access":"Customer Previlages",'User':u,'success':True}))
        else:
            return make_response(jsonify({'success':"False",'message':'Wrong Password'}))


class edit_profile(Resource):
    def patch(self):
        body=request.form
        f=request.files['profilepic']
        print(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        u=User.objects.get(username=body['username'])
        u.save(
        name=body['name'],
        profile_pic=secure_filename(f.filename)
        )
        u.save()
        return make_response(jsonify({'Message':'Profile Changed Successfully','profile':u}))






class items_functions(Resource):
    def get(self):
        i=item.objects()
        return make_response(jsonify({'message':'Here is the list of items available','items':i}))
    def post(self):
        body=request.get_json()
        u=User.objects().get(username=body['username'])
        if(u.scope=='customer'):
            return make_response(jsonify({'Message':'Permission Denied, You Dont have the clearance for this operation'}))
        i=item(
            itemID=uuid.uuid4(),
            itemname=body['itemname'],
            sellingprice=body['sellingprice'],
            costprice=body['costprice'],
            offer=body['offer']
        )
        i.save()
        return make_response(jsonify({'message':'Item Added Successfully','item':i}))
    def patch(self):
        body=request.get_json()
        i=None
        user=User.objects().get(username=body['username'])
        if(user.scope=='customer'):
            return make_response(jsonify({'message':'Customers not allowed to do this operation'}))
        try:
            i=item.objects.get(itemname=body['itemname'])
        except:
            pass
        if i==None:
            return make_response(jsonify({'Message':'ItemNotFound'}))
        i.sellingprice=body['sellingprice']
        i.costprice=body['costprice']
        i.offer=body['offer']
        i.save()
        return make_response(jsonify({'message':'Updated Item','Item':i}))
    


