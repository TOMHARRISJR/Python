
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'this is my secret key'

# Save files


@app.route('/')  # default url /
def display_form():
    # telling server what to show  render template("html file")
    return render_template("index.html")


@app.route('/result')  # <---- this is called url/ route (/result)
def result():
    # telling server what to show  render template("html file")
    return render_template("index1.html")


@app.route('/process', methods=["post"])
def form():
    session["Name"] = request.form["Name"]
    session["Language"] = request.form["Language"]
    session["Location"] = request.form["Location"]
    session["Comment"] = request.form["Comment"]
    return redirect('/result')  # redirecting back to a different url/ route


if __name__ == "__main__":
    app.run(debug=True)
