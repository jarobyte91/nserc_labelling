from engine import db

class LabelledExample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_index = db.Column(db.Integer)
    date = db.Column(db.String)
    author = db.Column(db.String)
    subreddit = db.Column(db.String)
    post = db.Column(db.String)
    gender = db.Column(db.Integer)
    employment = db.Column(db.Integer)
    student = db.Column(db.Integer)
    immigrant = db.Column(db.Integer)
    age = db.Column(db.Integer)
    relationship = db.Column(db.Integer)
    psychology = db.Column(db.String)

    def __repr__(self):
        return '<LabelledExample {}>'.format(self.index)
    
class UnlabelledExample(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    author = db.Column(db.String)
    subreddit = db.Column(db.String)
    post = db.Column(db.String)

    def __repr__(self):
        return '<UnlabelledExample {}>'.format(self.index)