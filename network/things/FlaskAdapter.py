from flask import Flask
from flask_restful import Api, Resource, reqparse


class Values(Resource):
    def get(self, key):
        return key, 200

    def post(self, key):
        return key, 201


class FlaskAdapter:

    def start(self):
        print("before")
        app = Flask(__name__)
        api = Api(app)
        print("prob here")
        api.add_resource(Values, "/<string:key>")
        print("prob not here")
        app.run(port=8080, threaded=True)
        print("after")

    def loop(self):
        pass

