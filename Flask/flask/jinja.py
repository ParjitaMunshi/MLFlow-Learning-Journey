from flask import Flask, render_template, request, redirect, url_for

### WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/success/<int:score>")
def success(score):
    res = "PASSED" if score >= 50 else "FAILED"
    return render_template('result.html', results=res)

@app.route("/successres/<int:score>")
def successres(score):
    res = "PASSED" if score >= 50 else "FAILED"
    exp = {'score': score, "res": res}
    return render_template('result1.html', results=exp)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html', results=score)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        
        # Correcting total_score calculation
        total_score = (science + maths + c + data_science) / 4
        return redirect(url_for('successres', score=int(total_score)))
    else:
        return render_template('getresult.html')

if __name__ == "__main__":
    app.run(debug=True)
