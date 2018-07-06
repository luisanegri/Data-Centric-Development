from flask import Flask, render_template, redirect, request, url_for, session
import os
from flask_pymongo import PyMongo
import bcrypt



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook_app'
app.config["MONGO_URI"] = 'mongodb://root:adminr00t@ds227481.mlab.com:27481/cookbook_app'

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')
    
    
@app.route("/login", methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'
    
    
@app.route("/register", methods=['POST','GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'Username already exists. Try another one!'

    return render_template('register.html')

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
        app.secret_key = 'mysecret'
        app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    