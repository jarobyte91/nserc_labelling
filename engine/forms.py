from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, InputRequired

class LabellingForm(FlaskForm):
    gender =  RadioField("What is the gender of the poster?", 
                          validators = [DataRequired()],
                          choices = [("Male", "Male"),
                                     ("Female", "Female"),
                                     ("Unknown", "Unknown")])
    employment =  RadioField("What is the employment status of the poster?", 
                             validators = [DataRequired()],
                             choices = [("Employed", "Employed"),
                                        ("Unemployed", "Unemployed"),
                                        ("Unknown", "Unknown")])
    age = StringField("What is the age of the poster?",
                      default = "Unknown",
                      validators = [DataRequired()])
    student =  RadioField("Is the poster a student?", 
                          validators = [DataRequired()],
                          choices = [("Student", "Student"),
                                     ("Not student", "Not student"),
                                     ("Unknown", "Unknown")])
    immigrant =  RadioField("Is the poster an immigrant?", 
                            validators = [DataRequired()],
                            choices = [("Immigrant", "Immigrant"),
                                       ("Not Immigrant", "Not Immigrant"),
                                       ("Unknown", "Unknown")])
    relationship = RadioField("Does the poster have a relationship?",
                              validators = [DataRequired()],
                              choices = [("Boyfriend", "Boyfriend"),
                                         ("Husband", "Husband"),
                                         ("Girlfriend", "Girlfriend"),
                                         ("Wife", "Wife"),
                                         ("Single", "Single"),
                                         ("Unknown", "Unknown")])
    psychology = StringField("Does the poster have a psychological disorder?",
                             validators = [DataRequired()],
                             default = "Unknown")
    submit = SubmitField("Submit")    
