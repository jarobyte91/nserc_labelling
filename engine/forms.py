from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, InputRequired

class LabellingForm(FlaskForm):
    gender =  RadioField("What is the gender of the poster?", 
                          validators = [DataRequired()],
                          choices = [(1, "Male"),
                                     (-1, "Female"),
                                     (0, "Unknown")])
    employment =  RadioField("What is the employment status of the poster?", 
                             validators = [DataRequired()],
                             choices = [(1, "Employed"),
                                        (-1, "Unemployed"),
                                        (0, "Unknown")])
    age = StringField("What is the age of the poster? (0 means unknown)",
                      default = 0,
                      validators = [DataRequired()])
    student =  RadioField("Is the poster a student?", 
                          validators = [DataRequired()],
                          choices = [(1, "Student"),
                                     (-1, "Not student"),
                                     (0, "Unknown")])
    immigrant =  RadioField("Is the poster an immigrant?", 
                            validators = [DataRequired()],
                            choices = [(1, "Immigrant"),
                                       (-1, "Not Immigrant"),
                                       (0, "Unknown")])
    submit = SubmitField("Submit")    
