# tests/test_robot_routes.py

import unittest
from flask import json
from app import app

class TestRobotRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def setUp(self):
        # Reset global variables before each test
        global robot_pos_x, robot_pos_y, robot_facing, is_placed
        robot_pos_x = None
        robot_pos_y = None
        robot_facing = None
        is_placed = False

    def test_place_route_success(self):
        response = self.client.post('/place', json={"x": 1, "y": 1, "facing": "NORTH"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)["status"], "success")

    def test_place_route_failure(self):
        response = self.client.post('/place', json={"x": -1, "y": 1, "facing": "NORTH"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["status"], "error")

    def test_move_route_success(self):
        self.client.post('/place', json={"x": 1, "y": 1, "facing": "NORTH"})
        response = self.client.get('/move')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["status"], "success")

    def test_move_route_failure(self):
        self.client.post('/place', json={"x": 4, "y": 4, "facing": "EAST"})
        response = self.client.get('/move')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["status"], "error")

    def test_rotate_left_route(self):
        self.client.post('/place', json={"x": 1, "y": 1, "facing": "NORTH"})
        response = self.client.get('/left')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["status"], "success")

    def test_rotate_right_route(self):
        self.client.post('/place', json={"x": 1, "y": 1, "facing": "NORTH"})
        response = self.client.get('/right')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["status"], "success")

    def test_report_route(self):
        self.client.post('/place', json={"x": 1, "y": 1, "facing": "NORTH"})
        response = self.client.get('/report')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["status"], "success")

if __name__ == "__main__":
    unittest.main()
