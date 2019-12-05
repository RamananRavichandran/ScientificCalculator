from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="static")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/sin_req")
def sin_req():
    return render_template('sin.html')

@app.route("/sin_res",methods=['POST'])
def sin_res():
        angle = request.form.get('input')
        c1 = ScientificCalc()
        result = c1.sin_func(angle)
        return render_template('sin_response.html',value=result)

if __name__=='__main__':
    app.run(debug=True)
