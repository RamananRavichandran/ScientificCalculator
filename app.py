from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__,template_folder="static")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/sineh_req")
def sineh_req():
    return render_template('sinh.html')

@app.route("/sineh_res",methods=['POST'])
def sinh_res():
        angle = request.form.get('input')
        c1 = ScientificCalc()
        result = c1.sine_h(angle)
        return render_template('sinh_response.html',value=result)

if __name__=='__main__':
    app.run(debug=True)
