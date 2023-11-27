from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.route("/")
def hello_world():
    return jsonify({"message": "Hello, world!"})
