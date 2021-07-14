from flask import Blueprint,render_template

updatecourses=Blueprint('updatecourses',__name__)


@updatecourses.route('/update')
def update():
    return render_template("updatecourse.html")