from flask import render_template, url_for, redirect, flash
from engine import app, db
from engine.forms import LabellingForm
from engine.models import LabelledExample, UnlabelledExample
import re
from itertools import zip_longest
import country_list
from random import choice

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def create_paragraphs(text):
    sentence_pattern = r"(?<=[a-z\)])\.(?=\s+?[A-Z])"
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    matches = re.split(sentence_pattern, text)
    if len(matches) > 5:
        g = list(grouper([p.strip() + "." for p in matches], 5, ""))
        return "".join(["<p>" + " ".join(l) + "</p>" for l in g])
    else: 
        return text

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
    data = choice(UnlabelledExample.query.all())
    author = data.author
    date = data.date
    subreddit = data.subreddit
    post = data.post
    original_text = data.post
    # highlight some patterns to improve readability
    ## age and sex
    post = highlight(r"([0-9]{2})\s+(year(s)? old|years|yo)", post, )
    post = highlight(r"[Ii]\s?.m\s?[0-9]{2}\b", post)
    post = highlight(r"[0-9]{2}[mfMF]|[mfMF][0-9]{2}", post)
    post = highlight(r"([\(\[])([0-9mfMF\/\s]{3,})([\)\]])", post)
    post = highlight(r"([Ff]e)?[Mm]ale", post)
    ## employment
    post = highlight(r"(work|(un)?employed|job)", post)
    ## immigration
    post = highlight(r"I\s+(am|'m)\s+from", post)
    post = highlight("|".join([country for code, country in country_list.countries_for_language("en")]), post)
    ## student
    post = highlight(r"[Ss]tudent|[Ss]chool|[Uu]niversity|[Cc]ollege", post)
    ## relationships
    post = highlight(r"([Gg]irl|[Bb]oy)friend|[Ww]ife|[Hh]usband|BF|bf|GF|gf", post)
    ## psychology
    post = highlight(r"[Aa]nxi(ety|ous)|[Dd]epress(ion|ed)|[Ss]uicid(e|al)|[Aa]ddict(ion|ed)?|[Ss]tress(ed)?|ADHD|adhd|PTSD|ptsd|ocd|OCD|bpd|BPD", post, "darkmagenta")
    post = highlight(r"[Tt]herap(y|ist)|[Ss]upport|[Mm]edic(al)?", post, "darkmagenta")
    post = create_paragraphs(post)
    form = LabellingForm()
    if form.validate_on_submit():
        r = LabelledExample(id = LabelledExample.query.count() + 1, 
                            original_index = data.index,
                            date = date, 
                            author = author,
                            subreddit = subreddit,
                            post = original_text,
                            gender = form.gender.data,
                            employment = form.employment.data,
                            student = form.student.data,
                            immigrant = form.immigrant.data,
                            age = form.age.data,
                            relationship = form.relationship.data,
                            psychology = form.psychology.data)
        db.session.add(r)
        db.session.delete(data)
        db.session.commit()
        flash("Thanks for your submission!")
        return redirect(url_for("index"))
    else:
        # flash("There was a problem with your submission, showing a new example")
        return render_template("label.html", 
                               date = date,
                               author = author,
                               subreddit = subreddit,
                               post = post,
                               form = form,
                               index = data.index)
    
