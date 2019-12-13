"""This module is used for main method"""
from __future__ import print_function
import argparse
import logging
from src.exception.unnecessary_parameter_exception import UnnecessaryParameterException
from src.driver.scientific_calc import ScientificCalc
from src.exception.method_not_found_exception import MethodNotFoundException

logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                       format='%(name)s - %(levelname)s - %(message)s - %(asctime)s '
                       '- %(lineno)d - %(module)s - %('
                       'funcName)s - %(pathname)s')


def main():
    """This main function is used to get input from user and call the scientific calculator
    functions, create object for scientific_calc class, passing parameters using Command Line
    and calling the method"""
    try:
        obj_power = ScientificCalc()
        parser = argparse.ArgumentParser()
        parser.add_argument('--function', type=str, required=True, nargs='+')
        args = parser.parse_args()
        method_name = args.function
        if method_name[0] == 'e_power_x':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            power = method_name[1]
            print(obj_power.exponential_func(power))
        elif method_name[0] == '10_power_x':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            power_val = method_name[1]
            print(obj_power.cal_power_ten(power_val))
        elif method_name[0] == 'x_power_y':
            if len(method_name) > 3:
                raise UnnecessaryParameterException
            input_base = method_name[1]
            input_power = method_name[2]
            final_answer = obj_power.var_initialization(input_base, input_power)
            print(final_answer)
        elif method_name[0] == 'tanh':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            res = obj_power.calculate_tanh(method_name[1])
            print(res)
        elif method_name[0] == 'sin':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            power = method_name[1]
            print(obj_power.sin_func(power))

        elif method_name[0] == 'cube_root':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            number = method_name[1]
            print(obj_power.cube_root(number))
        elif method_name[0] == 'square_root':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            x_value = method_name[1]
            print(obj_power.square_root(x_value))
        elif method_name[0] == 'rad':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            angle = method_name[1]
            print(obj_power.rad(angle))
        elif method_name[0] == 'one_by_x':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            number1 = method_name[1]
            print(obj_power.one_by_x(number1))
        elif method_name[0] == 'cos':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            number1 = method_name[1]
            print(obj_power.calculate_cos(number1))
        elif method_name[0] == 'tan':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            tan_result = method_name[1]
            print(obj_power.tan_fun(tan_result))
        elif method_name[0] == 'log':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            log_result = method_name[1]
            print(obj_power.logarithm(log_result))
        elif method_name[0] == 'sinh':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            sinh_input = method_name[1]
            print(obj_power.sine_h(sinh_input))
        elif method_name[0] == 'cosh':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            number = method_name[1]
            print(obj_power.trig_cosh(number))
        elif method_name[0] == 'ln':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            power = method_name[1]
            print(obj_power.ln_func(power))
        elif method_name[0] == 'add':
            add_list = []
            for key in range(1, len(method_name)):
                add_list.append(method_name[key])
            print(obj_power.addition(add_list))

        elif method_name[0] == 'sub':
            sub_list = []
            for key in range(1, len(method_name)):
                sub_list.append(method_name[key])
            print(obj_power.subtraction(sub_list))

        elif method_name[0] == 'mul':
            mul_list = []
            for key in range(1, len(method_name)):
                mul_list.append(method_name[key])
            print(obj_power.multiplication(mul_list))

        elif method_name[0] == 'div':
            div_list = []
            for key in range(1, len(method_name)):
                div_list.append(method_name[key])
            print(obj_power.division(div_list))

        elif method_name[0] == 'factorial':
            if len(method_name) > 2:
                raise UnnecessaryParameterException
            fact = method_name[1]
            print(obj_power.factorial(fact))
        else:
            raise MethodNotFoundException

    except IndexError as index:
        print(index)
        logging.exception(index)

    except UnnecessaryParameterException as parameter:
        logging.exception(parameter)

    except MethodNotFoundException as parameter:
        logging.exception(parameter)
