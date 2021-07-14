from flask import Blueprint,render_template

coursemanagements=Blueprint('coursemanagements', __name__)


@coursemanagements.route('/course')
def course():
    return render_template("coursemanagement.html")