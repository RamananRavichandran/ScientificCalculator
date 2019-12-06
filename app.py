from flask import Flask, render_template, request
from flask import (
    Flask,
    render_template,
    request)
from src.driver.scientific_calc import ScientificCalc
# Create the application instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/e_power_x_req')
def e_power_x_req():
    return render_template('e_power_x_req.html')

@app.route('/e_power_x_res', methods=['POST'])
def e_power_x_res():
        power_value=request.form['input']
        e_power_x_obj=ScientificCalc()
        result=e_power_x_obj.exponential_func(power_value)
        return render_template('e_power_x_res.html',value=result)
    # If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)