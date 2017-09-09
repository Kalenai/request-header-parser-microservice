from flask import Blueprint


parser = Blueprint('parser', __name__)

from . import resources
