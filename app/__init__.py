from flask import Flask

app = Flask(__name__)

from app import views
from app import userViews
from app import callCenterViews
from app import cartViews
from app import customerServiceViews
from app import  warehouseViews
from app import marketingDeptViews
from app import adminViews

