from typing import Text
from flask import Flask, jsonify
from flask.templating import render_template
from database import load_jobs_from_db
from sqlalchemy import text


app = Flask(__name__)


@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='DOTCONNECT')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
