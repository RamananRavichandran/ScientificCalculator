from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="Template")


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/cube_root_req")
def cube_root_req():
    return render_template('cube_root_req.html')

@app.route("/cube_root_res",methods=['POST'])
def cube_root_res():
    number1 = request.form.get('input')
    c1 = ScientificCalc()
    result = c1.cube_root(number1)
    return render_template('cube_root_res.html', value=result)

if __name__=='__main__':
    app.run(debug=True)
