from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    # github = "jhacks"
    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html" , first=first, gorilla=last, giraffe=github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/show-student-add-form")
def student_add():
    """Add a student."""
    hackbright.make_new_student(first_name, last_name, github)
    
    return  render_template("student-add.html")


@app.route("/add-student")
def student_add():

    first_name = request.form.args("firstname") # passing on name value from form to get the data
    last_name = request.form.args("lastname")
    GitHub = request.form.args("new_github")

    hackbright.make_new_student(first_name, last_name, github) # from hackbright.py file
    """Add a student."""

    return  render_template()


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
