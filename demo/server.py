# Import Flask to allow us to create our app
from flask import Flask, render_template
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    height = 200
    num_of_hellos = 300
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]

    return render_template("index.html", times=num_of_hellos, list=student_info, height=height)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)
