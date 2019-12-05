from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="static")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/tanh_req")
def tanh_req():
    return render_template('tanh.html')

@app.route("/tanh_res",methods=['POST'])
def tanh_res():
        angle = request.form.get('input')
        c1 = ScientificCalc()
        result = c1.calculate_tanh(angle)
        return render_template('tanh_response.html',value=result)

if __name__=='__main__':
    app.run(debug=True)
