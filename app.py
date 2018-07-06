from flask import Flask, render_template, redirect, request, url_for
import os
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook_app'
app.config["MONGO_URI"] = 'mongodb://root:adminr00t@ds227481.mlab.com:27481/cookbook_app'

mongo = PyMongo(app)



@app.route("/get_recipes")
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())
    

@app.route("/add_recipes")
def add_recipes():
    return render_template('addrecipes.html', categories=mongo.db.categories.find(), 
    difficulty=mongo.db.difficulty.find())
    
@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    # get recipes collection
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))





if __name__ == '__main__':
        app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    