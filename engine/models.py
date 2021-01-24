from engine import db

class LabelledExample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    author = db.Column(db.String)
    subreddit = db.Column(db.String)
    post = db.Column(db.String)
    gender = db.Column(db.Integer)
    employment = db.Column(db.Integer)
    student = db.Column(db.Integer)
    immigrant = db.Column(db.Integer)
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<LabelledExample {}>'.format(self.id)
    
class UnlabelledExample(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    author = db.Column(db.String)
    subreddit = db.Column(db.String)
    post = db.Column(db.String)

    def __repr__(self):
        return '<UnlabelledExample {}>'.format(self.id)