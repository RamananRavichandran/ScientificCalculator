from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/cos_req")
def calculate():
    return render_template('cos_req.html')

@app.route("/cos_res",methods=['POST'])
def response():
    if request.method == 'POST':
        angle = request.form['angle']
        calculate_cos_obj = ScientificCalc()
        result = calculate_cos_obj.calculate_cos(angle)
    return render_template('cos_res.html',value=result)

if __name__=='__main__':
    app.run(debug=True)