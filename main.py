import time
import queue
from db import db
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        log = request.get_json()
        db().db_insert(log)
        return "log accepted"
    else:
        return render_template('submit.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.get_data().decode('utf-8')
        logs = db().db_query(query)
        return jsonify(list(logs))
    else:
        logs = db().db_query()
        return render_template('search.html', logs=list(logs))

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080)
