from re import I
from flask import Flask
from datetime import datetime
from adminweb.controllers.addcourses import addcourses
from adminweb.controllers.getcourses import getcourses
from adminweb.controllers.coursemanagements import coursemanagements
from adminweb.controllers.updatecourses import updatecourses
from adminweb.model import db
def create_app():
    app=Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/admindb'
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.register_blueprint(getcourses)
    app.register_blueprint(addcourses)
    app.register_blueprint(coursemanagements)
    app.register_blueprint(updatecourses)
    return app


