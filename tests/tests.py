from flask import Flask
from flask-testing import TestCase
from app import app


class TestEndpoints(TestCase):
    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        return app

    def test_request_parser_endpoint(self):
        pass
