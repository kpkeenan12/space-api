from flask import Flask
from routes import cdm_api

app = Flask(__name__)
app.register_blueprint(cdm_api)