from flask import Flask
import requests

app = Flask(__name__)
root_api_url = "/api/"

@app.route(root_api_url)
def index():
    return "This is the index."

from apis.clickupapi import getKpis