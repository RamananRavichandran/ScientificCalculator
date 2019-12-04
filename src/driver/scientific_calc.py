"""This module is to execute scientific calculator functions"""
import math
import logging

logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                    format='%(name)s - %(levelname)s - %(message)s - %(asctime)s '
                           '- %(lineno)d - %(module)s - %('
                           'funcName)s - %(pathname)s')


class ScientificCalc:
    """This class is used to calculate the scientific operations"""

    def __init__(self):
        self.r_tan_f = 0
        self.power = 0
        self.result = 0
        self.base = 0
        self.angle = 0
        self.tanhx = 0
        self.n_value = 0
        self.x_value = 0
        self.degree = 0
        self.radian = 0
        self.number = 0
        self.number1 = 0
        self.sinh_of_x = 0

    @classmethod
    def cal_power_ten(cls, pow_value):
        """This function is used to calculate ten power x value"""
        try:
            cls.answer = 10 ** float(pow_value)
            return cls.answer
        except ValueError as value_error:
            logging.error(value_error)
            raise ValueError

    @classmethod
    def exponential_func(cls, power_value):
        """This function is used to calculate the exponential function"""
        try:
            cls.power = float(power_value)
            exp_value = 2.71828182846
            cls.result = exp_value ** cls.power
            return cls.result
        except ValueError as error:
            print(error)
            logging.exception(error)
            return "Please enter float or integer types input."

    @classmethod
    def x_power_y(cls, base_val, power_val):
        """if power value is 0 returns 1
        else recursively calls x_power_y function and returns the final answer"""
        cls.answer = 1
        if power_val == 0:
            return 1
        elif power_val % 2 == 0:
            return (cls.x_power_y(base_val, int(power_val / 2)) *
                          cls.x_power_y(base_val, int(power_val / 2)))
        else:
            if power_val > 0:
                return (base_val * cls.x_power_y(base_val, int(power_val / 2)) *
                              cls.x_power_y(base_val, int(power_val / 2)))
            else:
                return (cls.x_power_y(base_val, int(power_val / 2)) *
                              cls.x_power_y(base_val, int(power_val / 2))) / base_val

    @classmethod
    def var_initialization(cls, base_no, power_no):
        """initializing the variables"""
        try:
            base = float(base_no)
            power = int(power_no)
            return cls.x_power_y(base, power)
        except ValueError as error:
            logging.exception(error)
            return "Value Error"

    @classmethod
    def calculate_tanh(cls, angle):
        """A method to calculate tanh"""
        try:
            cls.angle = angle
            cls.angle = float(cls.angle)
            exponential = math.e
            coshx = ((exponential ** cls.angle) + (exponential ** -cls.angle))
            sinhx = ((exponential ** cls.angle) - (exponential ** -cls.angle))
            cls.tanhx = sinhx / coshx
            return cls.tanhx
        except ValueError as error:
            logging.exception(error)
            return "value error(enter a number)"

    @classmethod
    def sin_func(cls, angle):
        """This function is used to calculate the sin function"""
        try:
            cls.value = math.sin(float(angle))
            return cls.value
        except ValueError as error:
            logging.exception(error)
            print(error)
            return "Please enter float or integer types input."

    @classmethod
    def cube_root(cls, n_value):
        """function for Cube_Root"""
        cls.cube_value = 0
        try:
            v_value = int(n_value)
            if v_value > 0:
                cls.cube_value = v_value ** 0.33333333333333333333333333333333

            if v_value < 0:
                cls.cube_value = -(-v_value) ** 0.33333333333333333333333333333333

        except ValueError:
            logging.error(ValueError)
            return "ValueError"
        return cls.cube_value

    @classmethod
    def square_root(cls, x_value):
        """function for calculating square root"""
        try:
            cls.x_value = int(x_value)
            if cls.x_value >= 0:
                cls.square_value = cls.x_value ** 0.5
            elif cls.x_value < 0:
                cls.square_value = complex(cls.x_value) ** 0.5

        except ValueError:
            logging.error(ValueError)
            return "expecting integer value"
        return cls.square_value

    @classmethod
    def rad(cls, angle):
        """calculate radians"""
        try:
            cls.degree = float(angle)
            constpi = math.pi
            cls.radian = cls.degree * (constpi / 180)
            return cls.radian
        except ValueError as ex:
            logging.error(ex)
            return "Value Error"

    @classmethod
    def one_by_x(cls, number):
        """returns 1/x"""
        try:
            return float(1) / float(number)
        except ZeroDivisionError:
            logging.warning("division with zero cannot be performed")
            return "ZeroDivisionError"
        except ValueError:
            logging.warning("give an integer")
            return "ValueError"

    @classmethod
    def calculate_cos(cls, angle):
        """Function to calculate Cosine of an angle"""
        try:
            cls.angle = float(angle)
            cls.result = math.cos(cls.angle)
            return cls.result
        except ValueError as error:
            logging.exception(error)
            print(error)
            return "Please enter float or integer types input."

    @classmethod
    def tan_fun(cls, tan_angle):
        """check for the tangent value of a number"""
        try:
            tan_f = math.tan(float(tan_angle))
            r_tan_f = round(tan_f, 9)
            return r_tan_f

        except ValueError as value_error:
            logging.debug(value_error)

    @classmethod
    def logarithm(cls, number1):
        """check for log base 10 of a number"""
        try:
            cls.number1 = float(number1)
            if cls.number1 > 0:
                k = math.log10(cls.number1)
                return k
            elif type(cls.number1) != int:
                raise TypeError
            else:
                raise ValueError
        except ValueError as value_error:
            logging.error(value_error)
            print("enter positive values")
            return 'ValueError'
        except TypeError as type_error:
            logging.error(type_error)
            print("enter integer or float")
            return 'TypeError'

    @classmethod
    def sine_h(cls, x_value):
        """formula for finding sin"""
        exp_value = math.e
        try:
            cls.x_value = float(x_value)
            cls.sinh_of_x = ((exp_value ** cls.x_value) - (exp_value ** - cls.x_value)) / 2
            return cls.sinh_of_x

        except TypeError as type_error:
            print("Exception handled", type_error)
            logging.exception(type_error)

    @classmethod
    def trig_cosh(cls, number):
        """The function to calculate cosh"""
        try:
            if "." in str(number):
                number = float(number)
            else:
                number = int(number)
            calculate = 2.71828 ** number / 2 + 2.71828 ** -number / 2
            return calculate
        except ValueError as e_value:
            logging.exception(e_value)
            return "Value error"

    @classmethod
    def ln_func(cls, x_value):
        """The function to calculate ln"""
        try:
            if "." in str(x_value):
                x_value = float(x_value)
                if x_value > 0:
                    result = math.log(x_value)
                elif x_value == 0:
                    result = "infinity"
                else:
                    result = "-NAN-"
                return result
            else:
                x_value = int(x_value)
                if x_value > 0:
                    result = math.log(x_value)
                elif x_value == 0:
                    result = "infinity"
                else:
                    result = "-NAN-"
                return result
        except ValueError as v_error:
            logging.error(v_error)
            return "string is not accepted"

        except Exception as exception:
            logging.error(exception)
            return "Enter a valid value"
