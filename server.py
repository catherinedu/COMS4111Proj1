
"""
Columbia's COMS W4111.001 Introduction to Databases
Example Webserver
To run locally:
    python server.py
Go to http://localhost:8111 in your browser.
A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""
import os
  # accessible as a variable in index.html:
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, jsonify

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


prof = [
  {
    "last_name":'hi',
    "first_name":'yo',
    "course_name": "hii"
  }
]
print(prof[0]["first_name"])
DATABASEURI = "postgresql://yd2386:4613@35.243.220.243/proj1part2"

#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database,
# containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);""")
engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")


@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/home')
def home(name=None):
  return render_template('home.html')

@app.route('/search')
def search(name=None):
  return render_template('search.html', prof=prof)


@app.route('/search_item', methods=['GET', 'POST'])
def search_item():
  query = request.get_json()
  data = []
  dept = query[0]
  nugget = query[1].lower()
  # cmd = "SELECT Q.review AS p_review, R.review AS c_review, D.name AS department, P.last_name AS last_name, P.first_name AS first_name, C.name AS course_name FROM departments D, professors P, teaches T, Courses_in C, course_reviews_of R, professor_reviews_of Q WHERE D.did = c.did AND P.pid = T.pid AND T.cid = C.cid AND T.cid = R.cid AND P.pid = Q.pid AND D.nickname = :dept AND P.nugget = :nugget"
  if (dept == NULL) & (nugget != NULL):
      cmd = "SELECT Q.review AS p_review, R.review AS c_review, D.name AS department, P.last_name AS last_name, P.first_name AS first_name, C.name AS course_name FROM courses_in C, departments D, professors P, course_reviews_of R, professor_reviews_of Q, teaches T WHERE P.nugget = :nugget AND D.did = c.did AND P.pid = T.pid AND T.cid = C.cid AND T.cid = R.cid AND P.pid = Q.pid"
  elif (dept != NULL) & (nugget == NULL):
      cmd = "SELECT Q.review AS p_review, R.review AS c_review, D.name AS department, P.last_name AS last_name, P.first_name AS first_name, C.name AS course_name FROM courses_in C, departments D, professors P, course_reviews_of R, professor_reviews_of Q, teaches T WHERE D.nickname = :dept AND T.pid = P.pid AND T.cid = C.cid AND C.did = D.did"
  elif (dept != NULL) & (nugget != NULL):
      cmd = "SELECT Q.review AS p_review, R.review AS c_review, D.name AS department, P.last_name AS last_name, P.first_name AS first_name, C.name AS course_name FROM courses_in C, departments D, professors P, course_reviews_of R, professor_reviews_of Q, teaches T WHERE D.did = c.did AND P.pid = T.pid AND T.cid = C.cid AND T.cid = R.cid AND P.pid = Q.pid AND D.nickname = :dept AND P.nugget = :nugget "

  cursor = g.conn.execute(text(cmd), dept = dept, nugget = nugget)
  rows = cursor.fetchall()
  print(len(rows))
  print(cursor)
  for result in rows:
    print("yes")
    print(result['first_name'])
    data.append({'p_review': result['p_review'], 'c_review': result['c_review'], 'department': result['department'], 'last_name': result['last_name'], 'first_name': result['first_name'], 'course_name': result['course_name']})

  cursor.close()
  return jsonify(data=data)

@app.route('/search_item_prof', methods=['GET', 'POST'])
def search_item_prof():
  query = request.get_json()
  data = []
  last_name = query[0]
  first_name = query[1]
  print(last_name)
  print(first_name)
  cmd = "SELECT Q.review AS p_review, R.review AS r_review, D.name AS department, P.last_name AS last_name, P.first_name AS first_name, C.name AS course_name FROM departments D, professors P, teaches T, Courses_in C, course_reviews_of R, professor_reviews_of Q WHERE D.did = c.did AND P.pid = T.pid AND T.cid = C.cid AND T.cid = R.cid AND P.pid = Q.pid AND P.last_name = :last_name"
  cursor = g.conn.execute(text(cmd), last_name = last_name)
  rows = cursor.fetchall()
  print(len(rows))
  print(cursor)
  for result in rows:
    print("yes")
    print(result['first_name'])
    data.append({'p_review': result['p_review'], 'r_review': result['r_review'], 'department': result['department'], 'last_name': result['last_name'], 'first_name': result['first_name'], 'course_name': result['course_name']})

  cursor.close()
  return jsonify(data=data)
<<<<<<< HEAD



=======
  
>>>>>>> ea36fb9d2dd201d429978e5c85f68ace5f1baaf9


# # Example of adding new data to the database
# @app.route('/add', methods=['POST'])
# def add():
#   name = request.form['name']
#   g.conn.execute('INSERT INTO test(name) VALUES (%s)', name)
#   return redirect('/')



if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()
