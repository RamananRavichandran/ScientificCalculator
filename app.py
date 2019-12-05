from flask import (
    Flask,
    render_template,
    request
)
from src.driver.scientific_calc import ScientificCalc

# Create the application instance
app = Flask(__name__, template_folder="templates")


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """directed to home page"""
    return render_template("home.html")


@app.route('/tangent_req')
def tangent_req():
    return render_template("tangent_req.html")


@app.route('/tangent_res', methods=["POST"])
def tangent_res():
    angle_value = request.form.get("tan_value")
    flask_obj = ScientificCalc()
    tan_angle_value = flask_obj.tan_fun(angle_value)
    return render_template("tangent_res.html", result=tan_angle_value)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
