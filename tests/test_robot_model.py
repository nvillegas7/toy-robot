# tests/test_robot_model.py

import unittest
from models.robot_model import (
    place,
    move,
    rotate_left,
    rotate_right,
    report,
    validate_placement,
)

class TestRobotModel(unittest.TestCase):

    def setUp(self):
        # Reset global variables before each test
        global robot_pos_x, robot_pos_y, robot_facing, is_placed
        robot_pos_x = None
        robot_pos_y = None
        robot_facing = None
        is_placed = False

    def test_place_valid(self):
        result = place(1, 1, "NORTH")
        self.assertTrue(result)
        self.assertEqual(report(), "1, 1, NORTH")

    def test_place_invalid(self):
        result = place(-1, 1, "NORTH")
        self.assertFalse(result)
        self.assertEqual(report(), "Robot has not been placed yet!")

    def test_move_valid(self):
        place(1, 1, "NORTH")
        result = move()
        self.assertTrue(result)
        self.assertEqual(report(), "1, 2, NORTH")

    def test_move_invalid(self):
        place(4, 4, "EAST")
        result = move()
        self.assertFalse(result)
        self.assertEqual(report(), "4, 4, EAST")

    def test_rotate_left(self):
        place(1, 1, "NORTH")
        rotate_left()
        self.assertEqual(report(), "1, 1, WEST")

    def test_rotate_right(self):
        place(1, 1, "NORTH")
        rotate_right()
        self.assertEqual(report(), "1, 1, EAST")

    def test_validate_placement(self):
        place(1, 1, "NORTH")
        self.assertTrue(validate_placement()[0])
        place(5, 5, "NORTH")
        self.assertFalse(validate_placement()[0])

if __name__ == "__main__":
    unittest.main()
