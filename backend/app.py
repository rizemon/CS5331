from flask import Flask, request, redirect
from json import dumps

app = Flask(__name__)

captured_contents = []

@app.route("/", methods=["GET"])
def index():
    return "Home page"

@app.route("/unauthorized", methods=["GET"])
def unauthorized():
    return "Unauthorized page"

@app.route("/protected", methods=["GET"])
def protected():
    return "Protected page"

@app.route("/captured", methods=["GET", "POST"])
def captured():
    if request.method == "POST":
        content = request.form["content"]
        captured_contents.append(content)
        return "Appended: " + dumps([content])
        
    return dumps(captured_contents, indent=4)

@app.route("/redirected", methods=["GET"])
def redirected():
    host = request.headers["host"]
    return redirect("http://" + host, code=302)

@app.route("/reflected", methods=["GET"])
def reflected():
    user_agent = request.headers["user-agent"]
    return "User-Agent: " + user_agent
