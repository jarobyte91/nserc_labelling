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
    age = StringField("What is the age of the poster?",
                      default = "Unknown",
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
    relationship = RadioField("Does the poster have a relationship?",
                              validators = [DataRequired()],
                              choices = [(1, "Boyfriend"),
                                         (2, "Husband"),
                                         (-1, "Girlfriend"),
                                         (-2, "Wife"),
                                         (0, "Unknown")])
    psychology = StringField("Does the poster have a psychological disorder?",
                             validators = [DataRequired()],
                             default = "Unknown")
    submit = SubmitField("Submit")    
