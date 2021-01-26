from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, FileField, SubmitField
from wtforms.validators import DataRequired
 
# Form used to add to wishlist and visited forums
class AddLocation(FlaskForm):
  place_categories = [("Visited", "Visited"), ("Wish List", "Wish List")]
  name = StringField("Location Name", validators=[DataRequired()])
  description = StringField("Description")
  category = RadioField("Where Do You Want To Add Your Location?", choices=place_categories)
  submit = SubmitField("Add Location")

# Form used to add to ideas forums
class AddIdeas(FlaskForm):
  types = [("Country", "Country"), ("Region", "Region"), ("Activity", "Activity")]
  name2 = StringField("Location Name", validators=[DataRequired()])
  description2 = TextAreaField("Description")
  category2 = RadioField("Type", choices=types)
  submit2 = SubmitField("Add Location")