
from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'this is my secret key'


@app.route('/')
def counter():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 1
    return render_template("index.html")


@app.route('/addTwo', methods=["post"])
def add2Clicks():
    if "count" in session:
        session["count"] += 1
    # else:
    #     session["count"] = 1
    return redirect("/")


@app.route('/destroy', methods=["post"])
def remove_Counter():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
