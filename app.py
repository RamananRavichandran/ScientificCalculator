from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="templates")

@app.route("/")
def home():
    return render_template('home')

@app.route("/cosh_req")
def cosh_req():
    return render_template('cosh.html')

@app.route("/cosh_res",methods=['POST'])
def cosh_res():
        angle = request.form.get('input')
        c1 = ScientificCalc()
        result = c1.trig_cosh(angle)
        return render_template('cosh_response.html',value=result)

if __name__=='__main__':
    app.run(debug=True)

