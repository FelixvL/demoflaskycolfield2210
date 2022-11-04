from flask import Flask
import felix
import joris
import flavia 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/vanfelix")
def vanfelix():
    return felix.ditisvanfelix()


@app.route("/vanjoris")
def vanjoris():
    return joris.vanjoris()

@app.route("/vanflavia")
def vanflavia():
    return flavia.vanflavia()