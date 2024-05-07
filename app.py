from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define dimension of the table top
# Setting this here for so we can easily change if we want
# We can set these as env vars as needed depending on number
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Define global variables to store valuable data
# e.g. current robot position and direction its facing

robot_pos_x = None
robot_pos_y = None
robot_facing = None
is_placed = False  # Flag to check if robot has been placed

# Define movement offsets for each direction
# This will be used to efficiently check if robot will fall off
MOVEMENT_OFFSETS = {
    "NORTH": (0, 1), 
    "SOUTH": (0, -1), 
    "EAST": (1, 0), 
    "WEST": (-1, 0)
}

# Define directions in a circular list
# This will be used to easily rotate robot
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]


# Function to place the robot on the grid
def place(x, y, facing):
    global robot_pos_x, robot_pos_y, robot_facing, is_placed

    if (
        0 <= x < GRID_WIDTH
        and 0 <= y < GRID_HEIGHT
        and facing in ["NORTH", "SOUTH", "EAST", "WEST"]
    ):
        robot_pos_x = x
        robot_pos_y = y
        robot_facing = facing
        is_placed = True
        return True
    return False

# Function to validate if robot is on the grid
def validate_placement():
    if not is_placed:
        return False, "Robot has not been placed yet!"
    return True, ""

# Function to move the robot
def move():
    global robot_pos_x, robot_pos_y

    # Get movement offsets based on the current direction
    offset_x, offset_y = MOVEMENT_OFFSETS.get(robot_facing, (0, 0))
    # Calculate the new position after movement
    new_x = robot_pos_x + offset_x
    new_y = robot_pos_y + offset_y
    # Check if the new position is within bounds
    if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
        robot_pos_x = new_x
        robot_pos_y = new_y
        return True
    else:
        return False

# Function to rotate the robot left
def left():
    global robot_facing

    # Get the current index of the robot's facing direction
    current_index = DIRECTIONS.index(robot_facing)
    # Calculate the new index after rotating left
    new_index = (current_index - 1) % len(DIRECTIONS)
    # Update the robot's facing direction
    robot_facing = DIRECTIONS[new_index]
    return 

# Function to rotate the robot right
def right():
    global robot_facing

    # Get the current index of the robot's facing direction
    current_index = DIRECTIONS.index(robot_facing)
    # Calculate the new index after rotating right
    new_index = (current_index + 1) % len(DIRECTIONS)
    # Update the robot's facing direction
    robot_facing = DIRECTIONS[new_index]
    return

# Function to report the robot's current position and direction
def report():
    return f"{robot_pos_x}, {robot_pos_y}, {robot_facing}"


# API routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/place", methods=["POST"])
def place_robot():
    data = request.get_json()
    x = data.get("x")
    y = data.get("y")
    facing = data.get("facing")
    if place(x, y, facing):
        return jsonify(
            message="Successfully placed robot!",
            coordinates=report(),
        )
    else:
        return jsonify(message="Invalid placement!")


@app.route("/move", methods=["GET"])
def move_robot():
    success, message = validate_placement()
    if not success:
        return jsonify(message=message)
    if move():
        return jsonify(
            message="Onward!",
            coordinates=report(),
        )
    else:
        return jsonify(message="Cannot move, robot will fall off!")


@app.route("/left", methods=["GET"])
def left_rotate():
    success, message = validate_placement()
    if not success:
        return jsonify(message=message)
    left()
    return jsonify(message="Rotated Left!", coordinates=report())


@app.route("/right", methods=["GET"])
def right_rotate():
    success, message = validate_placement()
    if not success:
        return jsonify(message=message)
    right()
    return jsonify(message="Rotated Right!", coordinates=report())


@app.route("/report", methods=["GET"])
def report_robot():
    success, message = validate_placement()
    if not success:
        return jsonify(message=message)
    return jsonify(message=report(), coordinates=report())


if __name__ == "__main__":
    app.run(debug=True)
