from flask import Flask
from .models import db,login_manager
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object('config')

# UPLOAD_FOLDER = ''
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()

login_manager.init_app(app)
login_manager.login_view = 'login'

from app import models
from app import views
from app import userViews
from app import callCenterViews
from app import customerServiceViews
from app import  warehouseViews
from app import marketingDeptViews
from app import adminViews




