from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "world") # "world" is default argument
    return render_template("index.html", name=name)
    # 127.0.0.1:5000/?name=nelson