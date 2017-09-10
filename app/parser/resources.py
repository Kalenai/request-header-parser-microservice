import re
from werkzeug import useragents
from flask import jsonify, request
from . import parser


@parser.route('/')
def index():
    """
    Returns a JSON response with the user's IP address, browser language, and operating system information.
    """
    return jsonify(ipaddress=request.remote_addr,
                   language=request.accept_languages[0][0],
                   software=request.user_agent.string.split('(')[1].split(')')[0])
