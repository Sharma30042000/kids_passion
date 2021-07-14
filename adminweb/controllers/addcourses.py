from flask import Blueprint,render_template

addcourses=Blueprint('/addcourses',__name__)

@addcourses.route('/add')
def add():
    return render_template("add_course_form.html") 