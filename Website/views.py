from flask import Blueprint, render_template, request

from .FIBO_AI.Generate import Generate

views = Blueprint("views", __name__)
generate = Generate()


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/editor", methods=["GET", "POST"])
def editor():
    if request.method == "POST":
        query = request.form.get("query")
        image_url = generate.return_image(query)
        return render_template("editor.html", image_url=image_url)
    else:
        return render_template("editor.html")
