# Importing Flask class (Capital Letter)
from flask import flask

# Creating an instance and storing in a variable called 'app'
# 'name' is the first argument
app = Flask(__name__)


@app.route("/")
def index():
    return "Hellow World!"