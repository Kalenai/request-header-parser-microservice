from flask import jsonify, request
from . import parser


@parser.route('/')
def index():
    return jsonify(ipaddress=request.environ.get('REMOTE_ADDR'),
                   language=request.accept_languages[0][0],
                   software=request.user_agent.platform)
