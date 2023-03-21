from flask import Flask

app = Flask(__name__)

#import all of the route from the routes.py file into the current package
#app or.
from app import routes 