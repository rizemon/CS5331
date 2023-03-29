from flask import Flask, request, redirect
from json import dumps

app = Flask(__name__)

captured_contents = []

@app.route("/", methods=["GET"])
def index():
    return "<h1>Home Page</h1>\n" + \
        "<h2>Web Application is up and running.</h2>"

@app.route("/unauthorized", methods=["GET"])
def unauthorized():
    return "<h1>Unauthorized Page</h1>\n" + \
        "<h2>You are not authorized to view this page!</h2>"

@app.route("/protected", methods=["GET"])
def protected():
    return "<h1>Protected Page</h1>\n" + \
        "<h2>How are you here? This page is not supposed to be accessible!</h2>"

@app.route("/captured", methods=["GET", "POST"])
def captured():
    if request.method == "POST":
        content = request.form["content"]
        captured_contents.append(content)
        return "<h1>Captured Page</h1>\n" + \
            "Appended: " + dumps([content])
        
    return "<h1>Captured Page</h1>\n" + \
        dumps(captured_contents, indent=4)

@app.route("/redirected", methods=["GET"])
def redirected():
    host = request.headers["host"].split(",")[0]
    return redirect("http://" + host, code=302)

@app.route("/reflected", methods=["GET"])
def reflected():
    user_agent = request.headers["user-agent"].split(",")[0]
    return "<h1>Reflected Page</h1>\n" + \
        "User-Agent: " + user_agent
