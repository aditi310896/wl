# app.py
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()