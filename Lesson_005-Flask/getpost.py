from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    return "Welcome to the Jungle"

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if(request.method == "POST"):
        name = request.form['name']
        return f'Hello {name}!!'
    return render_template('form.html')

if(__name__ == "__main__"):
    app.run(debug = True)