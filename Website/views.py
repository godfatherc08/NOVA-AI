from flask import Blueprint, render_template


views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/editor")
def editor():
    return render_template("editor.html")
