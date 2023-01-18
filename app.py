from flask import Flask, render_template, request
import functions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    error = []
    # validate all fields are filled
    subject = request.form.get("subject")
    mye = request.form.get('mye')
    grade = request.form.get("grade")
    if not subject or not mye or not grade:
        error.append("All fields must be filled.")
        return render_template("error.html", error=error)
    
    error = [] # reset error to none

    # validate mye is float between 0-100 (there is probably a simpler way to do this)
    try:
        mye = float(mye)
        mye_float = True
    except:
        error.append("MYE score must be a number between 0 to 100.")
        mye_float = False
    if mye_float and (mye < 0 or mye > 100):
        error.append("MYE score must be a number between 0 to 100.")
    
    # validate grade
    grade = grade.upper()
    if grade not in 'ABCDESU' or len(grade)!= 1:
        error.append("Grade must be either A, B, C, D, E, S, or U.")

    # render error page if errors are present
    if error != []:
        return render_template("error.html", error=error)

    return render_template("result.html", promos=functions.promos(mye, grade), grade=grade, subject=subject)