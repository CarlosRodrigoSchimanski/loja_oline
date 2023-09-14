from flask import Flask
from .controllers import apllyRout

app = Flask(__name__)

app = apllyRout(app)