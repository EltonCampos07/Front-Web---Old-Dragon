from flask import Flask

app = Flask(__name__)

# Import routes and models
from app import routes, models