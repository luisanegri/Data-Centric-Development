from flask import Flask, render_template, redirect, request, url_for, session, g
import os 
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId



app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config["MONGO_DBNAME"] = 'cookbook_app'
app.config["MONGO_URI"] = 'mongodb://root:adminr00t@ds227481.mlab.com:27481/cookbook_app'

mongo = PyMongo(app)




@app.route("/get_recipes")
def get_recipes():
        return render_template('myrecipes.html', recipes=mongo.db.recipes.find())
        
    
    

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

@app.route("/read_recipe/<recipe_id>")
def read_recipe(recipe_id):
    the_recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories=mongo.db.categories.find()
    return render_template('readrecipe.html', recipe=the_recipe, categories=all_categories)


if __name__ == '__main__':
        app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    