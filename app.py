from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="templates")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/addition_req")
def addition_req():
    return render_template('addition.html')

@app.route("/addition_res",methods=['POST'])
def addition_res():
        list_add = []
        for a in range(0,1):
            num1 = request.form.get('input1')
            num2 = request.form.get('input2')
            list_add.append(num1)
            list_add.append(num2)
        c1 = ScientificCalc()
        result = c1.addition(list_add)
        return render_template('addition_response.html',value=result)

@app.route("/subtraction_req")
def subtraction_req():
    return render_template('subtraction.html')

@app.route("/subtraction_res",methods=['POST'])
def subtraction_res():
        list_sub = []
        for a in range(0,1):
            num1 = request.form.get('input1')
            num2 = request.form.get('input2')
            list_sub.append(num1)
            list_sub.append(num2)
        c1 = ScientificCalc()
        result = c1.subtraction(list_sub)
        return render_template('subtraction_response.html',value=result)

@app.route("/multiplication_req")
def multiplication_req():
    return render_template('multiplication.html')

@app.route("/multiplication_res",methods=['POST'])
def multiplication_res():
        list_mul = []
        for a in range(0,1):
            num1 = request.form.get('input1')
            num2 = request.form.get('input2')
            list_mul.append(num1)
            list_mul.append(num2)
        c1 = ScientificCalc()
        result = c1.multiplication(list_mul)
        return render_template('multiplication_response.html',value=result)

@app.route("/division_req")
def division_req():
    return render_template('division.html')

@app.route("/division_res",methods=['POST'])
def division_res():
        list_div = []
        for a in range(0,1):
            num1 = request.form.get('input1')
            num2 = request.form.get('input2')
            list_div.append(num1)
            list_div.append(num2)
        c1 = ScientificCalc()
        result = c1.division(list_div)
        return render_template('division_response.html',value=result)


if __name__=='__main__':
    app.run(debug=True)

