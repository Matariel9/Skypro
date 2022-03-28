from flask import Flask,render_template
from utils import *

app = Flask(__name__)

data = load_can("candidates.json")

print(data)

@app.route("/")
def index():
    return render_template('template.html', candidates=data)


@app.route("/candidate/<int:cid>")
def prof(cid):
    can = get_candidate(cid,data)
    return render_template('profile.html',candidate = can)

@app.route("/search/<name>")
def search_name(name):
    candidates = get_can_name(name,data)
    return render_template('search.html',candidates = candidates,candidates_len = len(candidates))

@app.route("/skill/<skill_name>")
def skill_search(skill_name):
    candidates = get_can_skill(skill_name,data)
    return render_template('skill.html',candidates = candidates,skill = skill_name,candidates_len = len(candidates))

app.run(debug=True)