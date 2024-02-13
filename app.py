from typing import Text
from flask import Flask, jsonify
from flask.templating import render_template
from database import engine, load_job_from_db, load_jobs_from_db

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


@app.route("/api/job/<id>")
def showjob(id):
  job = load_job_from_db(id)
  return jsonify(job)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)


@app.route("/job/<id>/apply")
def apply_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('thankyou.html', job=job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
