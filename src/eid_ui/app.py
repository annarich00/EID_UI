from dataclasses import asdict

from flask import Flask, jsonify, render_template

from .model import MissionState, plan_for_goal


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def dashboard():
        return render_template("index.html", state=asdict(MissionState()))

    @app.get("/api/plan/<goal>")
    def plan(goal: str):
        try:
            maneuver = plan_for_goal(goal)
        except ValueError as error:
            return jsonify(error=str(error)), 404
        return jsonify(asdict(maneuver))

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
