from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="static")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/square_root_req")
def square_root_req():
    return render_template('square_root.html')

@app.route("/square_root_res",methods=['POST'])
def square_root_res():
        value = request.form.get('input')
        c1 = ScientificCalc(value)
        result = c1.square_root(value)
        return render_template('square_root_response.html',value1=result)

if __name__=='__main__':
    app.run(debug=True)
