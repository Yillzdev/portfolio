import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")
BASE = Path(__file__).parent


def load_projects():
    """Projects live in projects.json: add an entry there when you finish one."""
    try:
        return json.loads((BASE / "projects.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=load_projects())


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/goal")
def goal():
    return render_template("goal.html")


if __name__ == "__main__":
    app.run(debug=True)
