from flask import Flask, request, jsonify

app = Flask(__name__)

# Define constants for grid size
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Define global variables to store robot position and direction
robot_x = None
robot_y = None
robot_facing = None
is_placed = False  # Flag to check if robot has been placed


# Function to place the robot on the grid
def place(x, y, facing):
    global robot_x, robot_y, robot_facing, is_placed
    if (
        0 <= x < GRID_WIDTH
        and 0 <= y < GRID_HEIGHT
        and facing in ["NORTH", "SOUTH", "EAST", "WEST"]
    ):
        robot_x = x
        robot_y = y
        robot_facing = facing
        is_placed = True
        return True
    return False


# Function to move the robot
def move():
    global robot_x, robot_y, robot_facing, is_placed
    if not is_placed:
        return False, "Robot has not been placed yet!"
    if robot_facing == "NORTH" and robot_y < GRID_HEIGHT - 1:
        robot_y += 1
        return True, ""
    # Implement similar checks for other directions
    return False, "Cannot move, robot will fall off!"


# Function to rotate the robot left
def left():
    global robot_facing, is_placed
    if not is_placed:
        return False, "Robot has not been placed yet!"
    # Implement rotation logic
    return True, ""


# Function to rotate the robot right
def right():
    global robot_facing, is_placed
    if not is_placed:
        return False, "Robot has not been placed yet!"
    # Implement rotation logic
    return True, ""


# Function to report the robot's current position and direction
def report():
    global robot_x, robot_y, robot_facing, is_placed
    if not is_placed:
        return False, "Robot has not been placed yet!"
    return True, f"{robot_x}, {robot_y}, {robot_facing}"


# API routes
@app.route("/place", methods=["POST"])
def place_robot():
    data = request.get_json()
    x = data.get("x")
    y = data.get("y")
    facing = data.get("facing")
    if place(x, y, facing):
        return jsonify(success=True, message="Robot placed successfully")
    else:
        return jsonify(success=False, message="Invalid placement!")


@app.route("/move", methods=["GET"])
def move_robot():
    success, message = move()
    return jsonify(success=success, message=message)


@app.route("/left", methods=["GET"])
def left_rotate():
    success, message = left()
    return jsonify(success=success, message=message)


@app.route("/right", methods=["GET"])
def right_rotate():
    success, message = right()
    return jsonify(success=success, message=message)


@app.route("/report", methods=["GET"])
def report_robot():
    success, message = report()
    if success:
        return jsonify(success=True, position=message)
    else:
        return jsonify(success=False, message=message)


if __name__ == "__main__":
    app.run(debug=True)
