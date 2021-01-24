from flask import render_template, url_for, redirect, flash
from engine import app, db
from engine.forms import LabellingForm
from engine.models import LabelledExample, UnlabelledExample
import re

def highlight(pattern, string, hl = "black"):
    matches = list(re.finditer(pattern, string))
    if matches is not []:
        starts = [m.start() for m in matches]
        ends = [m.end() for m in matches]
        output = ""
        for i, c in enumerate(string): 
            if i in starts:
                output += f'<span style="font-weight:bold;color:{hl}">' + c
            elif i in ends:
                output += "</span>" + c
            else: 
                output += c
    else:
        output = string
    return output

@app.route("/")
@app.route("/index")
def index():
    return redirect(url_for("label"))

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")

@app.route("/label", methods = ["GET", "POST"])
def label():
    data = UnlabelledExample.query.first()
    author = data.author
    date = data.date
    subreddit = data.subreddit
    post = data.post
    # highlight some patterns to improve readability
    post = highlight(r"([0-9]{2})\s+(year(s)? old|years|yo)", post)
    post = highlight(r"[\(\[]([0-9mfMF]{3})[\)\]]", post)
    post = highlight(r"(work|lost my job|don't have a job|am unemployed|left my job)", post)
    post = highlight(r"I\s+(am|'m)\s+from", post)
    form = LabellingForm()
    if form.validate_on_submit():
        r = LabelledExample(id = LabelledExample.query.count() + 1, 
                            date = date, 
                            author = author,
                            subreddit = subreddit,
                            post = post,
                            gender = form.gender.data,
                            employment = form.employment.data,
                            student = form.student.data,
                            immigrant = form.immigrant.data,
                            age = form.immigrant.data)
        db.session.add(r)
        db.session.delete(data)
        db.session.commit()
        flash("Thanks for your submission!")
        return redirect(url_for("index"))
    else:
        return render_template("label.html", 
                               date = date,
                               author = author,
                               subreddit = subreddit,
                               post = post,
                               form = form)
    
