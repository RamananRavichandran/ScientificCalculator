from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="templates")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/radian_req")
def radian_req():
    return render_template('rad.html')

@app.route("/radian_res",methods=['POST'])
def radian_res():
        angle = request.form.get('input')
        c1 = ScientificCalc()
        result = c1.rad(angle)
        return render_template('rad_response.html',value=result)

if __name__=='__main__':
    app.run(debug=True)

