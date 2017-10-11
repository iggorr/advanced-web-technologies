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

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
