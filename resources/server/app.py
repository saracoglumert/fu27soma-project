from flask import Flask, render_template, request, redirect
from datetime import datetime
import sys
import os
import inspect
import controller

CONF_ROOT_PATH = os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename))

app = Flask(__name__)

notifications = []

@app.route('/')
def main():
    endpoints = controller.Endpoints()
    return render_template('endpoints.html',title=controller.Node(controller.GetServerID()).name,endpoints=endpoints)

if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port, debug=False)