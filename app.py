from os import environ
from flask import Flask, render_template, request
from forms import AddLocation, AddIdeas

# Names the app
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_string"

# Uses home route to render homepage
@app.route("/")
def home():
  return render_template("home.html")

# Assigns lists used to store form data
wishlist_locations = []
wishlist_descriptions = []

# Uses wishlist route to render wishlist form and forum
@app.route("/wishlist", methods=["GET", "POST"])
def wishlist():
  add_location = AddLocation(csrf_enabled=False)
  if 'name' in request.form:
    wishlist_locations.append(request.form['name'])
    wishlist_descriptions.append(request.form['description'])
  return render_template("wishlist.html", template_form=add_location, wishlist_locations=wishlist_locations, wishlist_descriptions=wishlist_descriptions)

# Uses visited route to render visited form and forum
@app.route("/visited", methods=["GET", "POST"])
def visited():
  visited_locations = []
  visited_descriptions = []
  add_location_2 = AddLocation(csrf_enabled=False)
  if add_location_2.validate_on_submit():
    visited_locations.append(add_location_2.name.data)
    visited_descriptions.append(add_location_2.description.data)
  return render_template("visited.html", template_form_2=add_location_2, visited_locations=visited_locations, visited_descriptions=visited_descriptions)

# Uses ideas route to render ideas form and forum
@app.route("/location/ideas", methods=["GET", "POST"])
def ideas():
  add_ideas = AddIdeas(csrf_enabled=False)
  ideas_locations = []
  ideas_descriptions = []
  if add_ideas.validate_on_submit():
    ideas_locations.append(add_ideas.name.data)
    ideas_descriptions.append(add_ideas.description.data)
  return render_template("ideas.html",
  ideas=ideas, add_ideas=add_ideas, ideas_locations=ideas_locations, ideas_descriptions=ideas_descriptions)