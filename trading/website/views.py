from flask import Blueprint, render_template # standard roots for the website

views = Blueprint('views', __name__)

@views.route('/') # route decorator # whenever we hit this route we will run the function below
def home():
  return render_template("home.html") # render the home.html file