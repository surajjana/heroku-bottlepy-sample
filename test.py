import os
import time
import json
from bottle import Bottle

app = Bottle(__name__)

@app.route('/')
def test():
	return "Hello, World!! :-D";