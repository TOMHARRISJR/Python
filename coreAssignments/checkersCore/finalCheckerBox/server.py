from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index8x8.html')

@app.route('/8x8')
def hello_world_1():
    return render_template('index8x8_1.html')

@app.route('/8x4')
def hello_world_2():
    return render_template('index8x4.html')    


@app.route('/8x4b')
def hello_world_3():
    return render_template('index8x4_1.html')    

@app.route('/10x10')
def hello_world_4():
    return render_template('index10x10.html') 


@app.route('/10x10b')
def hello_world_5():
    return render_template('index10x10_1.html')      



if __name__=="__main__":
    app.run(debug=True, port=5000)

