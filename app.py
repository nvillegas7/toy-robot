from flask import Flask, render_template
from routes.robot_routes import robot_bp

app = Flask(__name__)
app.register_blueprint(robot_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
