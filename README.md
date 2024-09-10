# Toy Robot Flask App

## Description

This is a Flask web application that simulates the behavior of a toy robot moving on a tabletop. It provides a simple interface to interact with the robot by sending commands through HTTP requests.

## Features

- **Place Command**: Place the robot on the tabletop at a specified position and direction.
- **Move Command**: Move the robot one unit forward in the direction it is currently facing.
- **Left Command**: Rotate the robot 90 degrees to the left without changing its position.
- **Right Command**: Rotate the robot 90 degrees to the right without changing its position.
- **Report Command**: Get the current position and direction of the robot.

## Usage

1. Clone this repository:
    ```sh
    git clone https://github.com/nvillegas7/toy-robot.git
    ```

2. Navigate to the project directory:
    ```sh
    cd toy-robot
    ```

3. Build the Docker image:
    ```sh
    docker build -t my-flask-app .
    ```

4. Run the Docker container (Unit tests are automatically ran in this part as well):
    ```sh
    docker run -p 5001:5001 my-flask-app
    ```

5. Access the web interface:
    Open your web browser and go to [http://localhost:5001](http://localhost:5001) to access the Toy Robot interface.

## API Endpoints

- **POST /place**: Place the robot on the tabletop at a specified position.
  - **Parameters**:
    - `x`: X-coordinate of the position (0 to 4).
    - `y`: Y-coordinate of the position (0 to 4).
    - `direction`: Direction the robot is facing (NORTH, SOUTH, EAST, or WEST).

- **GET /move**: Move the robot one unit forward in the direction it is currently facing.

- **GET /left**: Rotate the robot 90 degrees to the left without changing its position.

- **GET /right**: Rotate the robot 90 degrees to the right without changing its position.

- **GET /report**: Get the current position and direction of the robot.
