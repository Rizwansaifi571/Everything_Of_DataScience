from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome Home !!"

@app.route("/result/<int:score>")
def result(score):
    res = ""
    if(score >= 50):
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template("result.html", result = res)


@app.route("/result1/<int:score>")
def result1(score):
    res = ""
    if(score >= 50):
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {'Score': score, 'Result' : res}
    return render_template("result1.html", result = exp)

@app.route("/result2/<int:score>")
def result2(score):
    return render_template("result2.html", result = score)


@app.route("/getresult", methods = ['GET', 'POST'])
def getresult():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['math'])
        dataScience = float(request.form['data_science'] )

        total_score = (science + math + dataScience) / 3
        return redirect(url_for('result1', score = total_score))
    
    return render_template("getresult.html")




if(__name__ == "__main__"):
    app.run(debug = True)