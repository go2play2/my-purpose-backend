import sys
from flask_script import Manager

from flask_twisted import Twisted
from app import create_app
from twisted.python import log


if __name__ == "main":
    app = create_app()
    twisted = Twisted(app)

    log = log.startLogging(sys.stdout)
    
    manager = Manager(app)
    manager.run()
