from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="templates")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/ln_req")
def ln_req():
    return render_template('ln.html')

@app.route("/ln_res",methods=['POST'])
def ln_res():
        angle = request.form.get('input')
        c1 = ScientificCalc()
        result = c1.ln_func(angle)
        return render_template('ln_response.html',value=result)

if __name__=='__main__':
    app.run(debug=True)