# tests/test_robot_controller.py

import unittest
from controllers.robot_controller import (
    handle_place,
    handle_move,
    handle_rotate_left,
    handle_rotate_right,
    handle_report
)

class TestRobotController(unittest.TestCase):

    def setUp(self):
        # Reset global variables before each test
        global robot_pos_x, robot_pos_y, robot_facing, is_placed
        robot_pos_x = None
        robot_pos_y = None
        robot_facing = None
        is_placed = False

    def test_handle_place_success(self):
        response = handle_place(1, 1, "NORTH")
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["coordinates"], "1, 1, NORTH")

    def test_handle_place_failure(self):
        response = handle_place(-1, 1, "NORTH")
        self.assertEqual(response["status"], "error")
        self.assertEqual(response["message"], "Invalid placement!")

    def test_handle_move_success(self):
        handle_place(1, 1, "NORTH")
        response = handle_move()
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["coordinates"], "1, 2, NORTH")

    def test_handle_move_failure(self):
        handle_place(4, 4, "EAST")
        response = handle_move()
        self.assertEqual(response["status"], "error")
        self.assertEqual(response["message"], "Cannot move, robot will fall off!")

    def test_handle_rotate_left(self):
        handle_place(1, 1, "NORTH")
        response = handle_rotate_left()
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["coordinates"], "1, 1, WEST")

    def test_handle_rotate_right(self):
        handle_place(1, 1, "NORTH")
        response = handle_rotate_right()
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["coordinates"], "1, 1, EAST")

    def test_handle_report(self):
        handle_place(1, 1, "NORTH")
        response = handle_report()
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["coordinates"], "1, 1, NORTH")

if __name__ == "__main__":
    unittest.main()
