from flask import Flask,render_template
from utils import *

app = Flask(__name__)

data = load_can("candidates.json")

print(data)

@app.route("/")
def index():
    return render_template('template.html', candidates=data)

app.run(debug=True)