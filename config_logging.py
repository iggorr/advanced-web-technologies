import ConfigParser, logging

from logging.handlers import RotatingFileHandler
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def root():
  this_route = url_for('.root')
  app.logger.info("Logging a test message from" + this_route)
  return "Hello Napier from the configuration testing app (now with added logging)"

@app.route('/config/')
def config():
  str = []
  str.append('Debug:' + app.config['DEBUG'])
  str.append('port:' + app.config['port'])
  str.append('url:' + app.config['url'])
  str.append('ip_address:' + app.config['ip_address'])
  return '\t'.join(str)

def init(app):
  config = ConfigParser.ConfigParser()
  try:
    config_location = 'etc/logging.cfg'
    config.read(config_location)

    app.config['DEBUG'] = config.get('config', 'debug')
    app.config['ip_address'] = config.get('config', 'ip_address')
    app.config['port'] = config.get('config', 'port')
    app.config['url'] = config.get('config', 'url')
    
    app.config['log_file'] = config.get('logging', 'name')
    app.config['log_location'] = config.get('logging', 'location')
    app.config['log_level'] = config.get('logging', 'level') 
   
  except:
    print "Could not read configs from: ", config_location

def logs(app):
  log_pathname = app.config['log_location'] + app.config['log_file']
  file_handler = RotatingFileHandler(log_pathname, maxBytes=1024 * 1024 * 10, backupCount=1024)
  file_handler.setLevel(app.config['log_level'])
  formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(message)s")
  file_handler.setFormatter(formatter)
  app.logger.setLevel( app.config['log_level'] )
  app.logger.addHandler(file_handler)

if __name__ == '__main__':
  init(app)
  logs(app)
  app.run(
    host = app.config['ip_address'],
    port = int(app.config['port']))
