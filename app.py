from distutils import errors
import requests
from flask import Flask, render_template, request,redirect,url_for
from django.contrib.sites import requests
from flask import (
    Flask,
    render_template,
    request)

# Create the application instance
app = Flask(__name__, template_folder="static")

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/e_power_x_req')
def e_power_x_req():
    return render_template('e_power_x_req.html')

@app.route('/e_power_x_res', methods=['POST'])
def e_power_x_res():
        power_value=request.form.get('input')
        power=float(power_value)
        exp_value = 2.71828182846
        result=exp_value**power
        return render_template('e_power_x_res.html',result=result)
    # If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)