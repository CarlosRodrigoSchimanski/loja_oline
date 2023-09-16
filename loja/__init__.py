from flask import Flask, Blueprint
from .user.rotas import usuario_bluprint

app = Flask(__name__)

app.register_blueprint(usuario_bluprint)