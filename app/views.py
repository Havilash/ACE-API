from flask import Blueprint, render_template, flash, request, abort, jsonify
from .functions import *


views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@views.route('/temp', methods=['GET'])
def temp():
    celsius = request.args.get('celsius', type=float)
    if celsius is None:
        abort(400, description="Parameter 'celsius' is invalid")
    return jsonify({"kelvin": celsius_to_kelvin(celsius), "celsius": celsius})


@views.route('/prime', methods=['GET'])
def prime():
    limit = request.args.get('limit', type=int)
    if limit is None or not (0 <= limit <= 10000):
        abort(400, description="Parameter 'limit' is invalid")
    return jsonify(primes(limit))


@views.route('/number', methods=['GET'])
def number():
    n = request.args.get('n', type=int)
    if n is None or not (0 <= n <= 250):
        abort(400, description="Parameter 'n' is invalid")
    return jsonify(fibonacci(n))