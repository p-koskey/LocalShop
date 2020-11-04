#Create Blueprint object and initialize it with a name
from flask import Blueprint

home = Blueprint('home', __name__)

from . import views