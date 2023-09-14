from flask import Flask
from .rout import apllyRout

app = Flask(__name__)

app = apllyRout(app)