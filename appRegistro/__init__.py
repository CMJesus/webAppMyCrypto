# ENTRADA:
from flask import Flask
# CREDENTIALS:
app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")

from appRegistro.views import *



