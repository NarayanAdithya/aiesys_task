from app.models import item
from flask import redirect,render_template
from app import app,api
from app.endpoints import signup,signin,items_functions,edit_profile

api.add_resource(signup,'/signup')
api.add_resource(signin,'/signin')
api.add_resource(items_functions,'/items')
api.add_resource(edit_profile,'/edit_profile')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')