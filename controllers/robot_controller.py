from models.robot_model import (
    place as model_place,
    move as model_move,
    rotate_left as model_rotate_left,
    rotate_right as model_rotate_right,
    report as model_report,
    validate_placement as model_validate_placement
)

def handle_place(x, y, facing):
    if model_place(x, y, facing):
        return {
                    "status": "success", 
                    "coordinates": model_report(), 
                    "message": "Successfully placed robot!"
                }
    return {"status": "error", "message": "Invalid placement!"}

def handle_move():
    success, message = model_validate_placement()
    if not success:
        return {"status": "error", "message": message}
    
    if model_move():
        return {"status": "success", "coordinates": model_report(), "message": "Onward!"}
    return {"status": "error", "message": "Cannot move, robot will fall off!"}

def handle_rotate_left():
    success, message = model_validate_placement()
    if not success:
        return {"status": "error", "message": message}
    
    model_rotate_left()
    return {"status": "success", "coordinates": model_report(), "message": "Rotated left!"}

def handle_rotate_right():
    success, message = model_validate_placement()
    if not success:
        return {"status": "error", "message": message}
    
    model_rotate_right()
    return {"status": "success", "coordinates": model_report(), "message": "Rotated right!"}

def handle_report():
    success, message = model_validate_placement()
    if not success:
        return {"status": "error", "message": message}
    
    return {"status": "success", "coordinates": model_report(), "message": model_report()}
