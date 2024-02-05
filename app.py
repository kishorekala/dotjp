from flask import Flask, jsonify
from flask.templating import render_template

app = Flask(__name__)

JOBS = [
    {
        'id': '1',
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': '2',
        'title': 'Data Scintist',
        'location': 'Hyderabad, India',
        'salary': 'Rs. 20,00,000'
    },
    {
        'id': '3',
        'title': 'Frong End Engineer',
        'location': 'Delhi, India'
    },
    {
        'id': '4',
        'title': 'Backend Enigeer',
        'location': 'Vizag, India'
    },
]


@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS, company_name='Dot')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
