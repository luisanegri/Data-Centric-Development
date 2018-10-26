
# CookBook Web App
Demo: https://cookbook-app-flask.herokuapp.com/

## Overview

> A web application created in Python and Flask. 

## UX

This website was created with the intention to store and share recipes with other users.
The home page shows the recipes categories, and allows the user to choose between Breakfast, Lunch, Dinner and Snacks. 
When clicking on any category, the user can view a list of recipes from that specific category. The user can choose a specific recipe from the list where it will be displayed more details about the recipe such as: Category, Serving, Time of preparation, difficulty level, ingredients and cooking method.
This page also allows the user to delete or edit the recipe.
On the navbar the user have access to all recipes, without categories. There's also a link that brings to a form to add a new recipe.

## Features

* Create new recipes - recipe name, category, level of difficulty, servings, preparation time, method, ingredients.
* Read recipes 
* Edit recipes
* Delete recipes

## Technologies Used

* [Bootstrap](https://getbootstrap.com/)
    * CSS framework to style and create responsive design 
* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
    * Python microframework
* [MongoDB](https://www.mongodb.com/)
    * NoSQL database
* [MLab](https://mlab.com/) 
    * MongoDB cloud database service where the data is stored
* [Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/)
    * Connects Flask to MongoDB

## Testing

All the CRUD actions were tested and are working as it should.
When updating a recipe the same is duplicated, this will be fixed later. I've added a delete button on the card so it can be deleted easily instead of the need to go to the recipe page to do so.
The responsiveness was tested on every page.
Every link was tested and works properly.

## Deployment

* This project was deployed at Heroku

1. Create requirements.txt 

        pip3 freeze --local requirements.txt
        
2. Create Procfile

        echo web: python app.py > Procfile
        
3. Create [Heroku](https://www.heroku.com/) App 
4. Set Config Vars adding IP and PORT on Heroku app settings

        IP 0.0.0.0
        PORT 5000
        
5. Login to Heroku on the terminal

        Heroku login
        
6. Deploy to Heroku

        Scale the app's web process to 1 dyno: heroku ps:scale web=1
        git remote add https://git.heroku.com/cookbook-app-flask.git
        git push heroku master




