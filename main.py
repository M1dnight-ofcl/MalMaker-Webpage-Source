import flask as f
from datetime import datetime
from colorama import Fore as color

version = "v0.1"
appname = "MalMaker Home"
author =  "M1dnightDev"

class FlaskApp(f.Flask):
  def __init__(self):
    super().__init__(__name__)

    print("%s\nversion %s\nby %s" %(appname, version, author))
    print("%s|%s| server has been initialized%s" %(color.BLUE, datetime.now(), color.RESET))
    
    @self.route('/')
    def home():
      return f.render_template("index.html", appname=appname)

  def __del__(self):
    print("%s|%s| server has been shutdown" %(color.RED, datetime.now()))

  def start(self):
    print("%s|%s| server has been started%s" %(color.GREEN, datetime.now(), color.RESET))
    self.run(host='0.0.0.0', port=81)

App = FlaskApp() # initialize class
App.start()      # start app