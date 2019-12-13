from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="static")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/one_by_x_req")
def one_by_x_req():
    return render_template('one_by_x.html')

@app.route("/one_by_x_res",methods=['POST'])
def one_by_x_res():
        number = request.form.get('input')
        ca1c = ScientificCalc()
        result = ca1c.one_by_x(number)
        return render_template('one_by_x_response.html',value=result)

if __name__=='__main__':
    app.run(debug=True)
