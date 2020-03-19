from flask import Flask, jsonify
from tinydb import TinyDB, Query
import os
import datetime
from flask_api import status

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/events/count')
def events_count():
    db = TinyDB('db.json')
    db_len = (len(db) + 1)
    db.insert({"counter": db_len, "datetime": str(datetime.datetime.utcnow())})
    return 'OK'

@app.route('/events/show')
def events_show():
    db = TinyDB('db.json')
    resp = db.search(Query().counter.exists())
    return jsonify(resp)

    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)