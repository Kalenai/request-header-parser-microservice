from flask import jsonify
from . import parser


@parser.route('/')
def index():
    return jsonify(hello="world")
