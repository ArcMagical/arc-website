from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Moscow, Russia',
    'salary': 'RUB 680,000'
  },
  {
    'id': 2,
    'title': 'Backend Engineer',
    'location': 'Saint Petersburg, Russia',
    'salary': 'RUB 250,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    
  },
  {
    'id': 4,
    'title': 'Data Analyst',
    'location': 'San Francisco, USA',
    'salary': '$77000'
  },
]

@app.route('/home')
def hello_arc():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='Arc')

@app.route('/application')
def application():
  return render_template('application.html',
                         company_name='Arc')

@app.route('/api/jobs')
def list_jobs():
  return jsonify()
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)


  

