from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def root():
  return "Root route"

@app.route("/hello/")
def hello():
  name = request.args.get('name', '')
  if name == '':
    return "Hello Napier"
  else:
    return "Hello %s" % name

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

@app.route('/req/', methods=['GET', 'POST'])
def req():
  print request.method, request.path, request.form
  return "Request info in logs bich"

@app.route('/account/', methods=['GET', 'POST'])
def account():
  if request.method == 'POST':
    print request.form
    name = request.form['name']
    return "Hello %s" % name
  else:
    page ='''
    <html><body>
      <form action="" method="post" name="form">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name"/>
        <input type="submit" name="suibmit" id="submit"/>
      </form>
      </body></html>'''

    return page

@app.route("/hi/<name>")
def hi(name):
  return "Hi %s" % name

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
  return str(first+second)

@app.route("/display/")
def display():
  return '<img src="'+url_for('static', filename='uploads/file.png')+'"/>'

@app.route("/upload/", methods=['POST', 'GET'])
def upload():
  if request.method == 'POST':
    f = request.files['datafile']
    f.save('static/uploads/file.png')
    return "File Uploaded!"
  else:
    page='''
    <html>
    <body>
    <form action="" method="post" name="form" enctype="multipart/form-data">
      <input type="file" name="datafile" />
      <input type="submit" name="submit" id="submit"/>
    </form>
    </body>
    </html>
    '''
    return page, 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
