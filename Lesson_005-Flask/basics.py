from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to The Rizz World..You know i am the best."

@app.route('/love')
def obsession():                    # route function mein call kr rhe hai
    return "You Know I love my self Because i am the best."

@app.route('/index')
def index():
    return "<html><h1>Welcome To index Page</h1></html>"

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug = True)