
# CookBook Web App
Demo: https://cookbook-app-flask.herokuapp.com/

## Overview

> A web application created in Python and Flask. 

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




