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


@app.route('/x_power_y_request')
def x_power_y_request():
    return render_template("x_power_y_req.html")


@app.route('/x_power_y_response', methods=["POST"])
def x_power_y_response():
    power_value = request.form.get("x_value")
    base_value = request.form.get("y_value")
    flask_obj = ScientificCalc()
    x_power_y_value = flask_obj.var_initialization(power_value, base_value)
    return render_template("x_power_y_res.html", result=x_power_y_value)


@app.route('/10_power_x_request')
def ten_power_x_request():
    return render_template("10_power_x_req.html")


@app.route('/10_power_x_response', methods=["POST"])
def ten_power_x_response():
    x_value = request.form.get("value_x")
    flask_obj = ScientificCalc()
    ten_power_x_value = flask_obj.cal_power_ten(x_value)
    return render_template("x_power_y_res.html", result=ten_power_x_value)


@app.route('/factorial_request')
def factorial_request():
    return render_template("factorial_req.html")


@app.route('/factorial_response', methods=["POST"])
def factorial_response():
    f_value = request.form.get("fact_value")
    flask_obj = ScientificCalc()
    fact_result = flask_obj.factorial(f_value)
    return render_template("factorial_res.html", result=fact_result)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
