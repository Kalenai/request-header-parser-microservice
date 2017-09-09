from flask import Flask
from app.parser import parser


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(parser)

    return app
