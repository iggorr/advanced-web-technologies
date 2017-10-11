from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def root():
  return "Root route"

@app.route("/hello")
def hello():
  return "Hello Napier"

@app.route("/goodbye/")
def goodbye():
  return "Aw leaving so soon"

@app.route("/private/")
def private():
  #Test if logged in failed
  return redirect(url_for('login'))

@app.route("/login/")
def login():
  return "Please log in babe"

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page omg", 404

@app.route('/force404/')
def force404():
  abort(404)

@app.route('/static-example/img')
def static_example_img():
  start = '<img src="'
  url = url_for('static', filename='vmask.jpg')
  end = '">'
  return start+url+end, 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
