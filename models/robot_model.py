# models/robot_model.py

# Define dimension of the table top
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Define global variables to store robot state
robot_pos_x = None
robot_pos_y = None
robot_facing = None
is_placed = False

# Define movement offsets for each direction
MOVEMENT_OFFSETS = {
    "NORTH": (0, 1), 
    "SOUTH": (0, -1), 
    "EAST": (1, 0), 
    "WEST": (-1, 0)
}

# Define directions in a circular list
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

def place(x, y, facing):
    global robot_pos_x, robot_pos_y, robot_facing, is_placed

    if (
        0 <= x < GRID_WIDTH
        and 0 <= y < GRID_HEIGHT
        and facing in DIRECTIONS
    ):
        robot_pos_x = x
        robot_pos_y = y
        robot_facing = facing
        is_placed = True
        return True
    is_placed = False
    return False

def move():
    global robot_pos_x, robot_pos_y

    if not is_placed:
        return False

    offset_x, offset_y = MOVEMENT_OFFSETS.get(robot_facing, (0, 0))
    new_x = robot_pos_x + offset_x
    new_y = robot_pos_y + offset_y

    if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
        robot_pos_x = new_x
        robot_pos_y = new_y
        return True
    return False

def rotate_left():
    global robot_facing

    if not is_placed:
        return

    current_index = DIRECTIONS.index(robot_facing)
    new_index = (current_index - 1) % len(DIRECTIONS)
    robot_facing = DIRECTIONS[new_index]

def rotate_right():
    global robot_facing

    if not is_placed:
        return

    current_index = DIRECTIONS.index(robot_facing)
    new_index = (current_index + 1) % len(DIRECTIONS)
    robot_facing = DIRECTIONS[new_index]

def report():
    if not is_placed:
        return "Robot has not been placed yet!"
    return f"{robot_pos_x}, {robot_pos_y}, {robot_facing}"

def validate_placement():
    if not is_placed:
        return False, "Robot has not been placed yet!"
    return True, ""
