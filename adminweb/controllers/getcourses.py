from flask import Flask,render_template
from flask.blueprints import Blueprint
from flask import Blueprint,render_template

getcourses=Blueprint('getcourses',__name__)

@getcourses.route('/get')
def get():
    return render_template("get_course.html")