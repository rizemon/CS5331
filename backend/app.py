from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Home page"

@app.route("/unauthorized", methods=["GET"])
def unauthorized():
    return "Unauthorized page"

@app.route("/protected", methods=["GET"])
def protected():
    return "Protected page"
