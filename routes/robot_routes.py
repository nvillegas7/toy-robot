# routes/robot_routes.py

from flask import Blueprint, request, jsonify
from controllers.robot_controller import (
    handle_place,
    handle_move,
    handle_rotate_left,
    handle_rotate_right,
    handle_report
)

robot_bp = Blueprint('robot', __name__)

@robot_bp.route("/place", methods=["POST"])
def place():
    data = request.get_json()
    x = data.get("x")
    y = data.get("y")
    facing = data.get("facing")
    
    if x is None or y is None or facing is None:
        return jsonify(message="Missing required parameters"), 400
    
    response = handle_place(x, y, facing)
    status_code = 201 if response["status"] == "success" else 400
    return jsonify(response), status_code

@robot_bp.route("/move", methods=["GET"])
def move():
    response = handle_move()
    status_code = 200 if response["status"] == "success" else 400
    return jsonify(response), status_code

@robot_bp.route("/left", methods=["GET"])
def rotate_left():
    response = handle_rotate_left()
    status_code = 200 if response["status"] == "success" else 400
    return jsonify(response), status_code

@robot_bp.route("/right", methods=["GET"])
def rotate_right():
    response = handle_rotate_right()
    status_code = 200 if response["status"] == "success" else 400
    return jsonify(response), status_code

@robot_bp.route("/report", methods=["GET"])
def report():
    response = handle_report()
    status_code = 200 if response["status"] == "success" else 400
    return jsonify(response), status_code
