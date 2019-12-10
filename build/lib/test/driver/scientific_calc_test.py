"""This module is used to unit test the scientific operation"""
import unittest
import math
from src.driver.scientific_calc import ScientificCalc


class ScientificCalcTest(unittest.TestCase):
    """class for unittesting"""

    def test_tanh_integer(self):
        """test case for tanh(4)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(4), 0.9993292997390669)

    def test_tanh_zero(self):
        """test case for tanh(0)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(0), 0.0)

    def test_tanh_integer500(self):
        """test case for tanh(500)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(500), 1.0)

    def test_tanh_negative(self):
        """test case for tanh(-14)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(-14), -0.9999999999986172)

    def test_tanh_float(self):
        """test case for tanh(8.9)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(8.1), 0.9999998157280002)

    def test_tanh_fnegative(self):
        """test case for tanh(-55.7)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(-55.7), -1.0)

    def test_tanh_string(self):
        """test case for tanh(-55.7)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh("sss"), "value error(enter a number)")

    def test_10_power_x_pos_power(self):
        """This function is used to unit test the scientific operation 10 power x
         for positive power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(2), 10 ** 2)

    def test_10_power_x_neg_power(self):
        """This function is used to unit test the scientific operation 10 power x
        for negative power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(-2), 10 ** (-2))

    def test_10_power_x_zero_power(self):
        """This function is used to unit test the scientific operation 10 power x
        for zero power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(0), 10 ** 0)

    def test_10_power_x_pos_dec_power(self):
        """This function is used to unit test the scientific operation 10 power x
        for positive_float power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(2.2), 10 ** 2.2)

    def test_10_power_x_neg_dec_power(self):
        """This function is used to unit test the scientific operation 10 power x
        for negative_float power value"""
        calculate_ten_power = ScientificCalc()
        self.assertEqual(calculate_ten_power.cal_power_ten(-2.2), 10 ** (-2.2))

    def test_10_power_x_exception_power(self):
        """This function is used to unit test the scientific operation 10 power
        for negative_float power value"""
        calculate_ten_power = ScientificCalc()
        with self.assertRaises(ValueError):
            calculate_ten_power.cal_power_ten('accenture')

    def test_10_power_x_inverse(self):
        """This function is used to test for the inverse of scientific operation
        10 power x"""
        calculate_ten_power = ScientificCalc()
        value = calculate_ten_power.cal_power_ten(2)
        inverse = math.log10(value)
        self.assertEqual(inverse, 2)

    def test_e_power_x_positive_exp(self):
        "When the input is positive integer"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(2), 2.71828182846 ** 2)

    def test_e_power_x_negative_exp(self):
        "When the input is negative integer"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(-2), 2.71828182846 ** -2)

    def test_e_power_x_zero_exp(self):
        "When the input is zero"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(0), 2.71828182846 ** 0)

    def test_e_power_x_pos_decimal_exp(self):
        "When the input is positive decimal"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(8.6), 2.71828182846 ** 8.6)

    def test_e_power_x_neg_decimal_exp(self):
        "When the input is negative decimal"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(-8.6), 2.71828182846 ** -8.6)

    def test_e_power_x_try_except(self):
        "Test case for try and except"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func('accenture'),
                         "Please enter float or integer types input.")

    def test_x_power_y_posint_posint(self):
        """When both the input is positive integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2, 2), pow(2, 2))

    def test_x_power_y_negint_posint(self):
        """When power is positive integer and base is negative integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2, 2), pow(-2, 2))

    def test_x_power_y_negint_negint(self):
        """When both the input is negative integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2, -2), pow(-2, -2))

    def test_x_power_y_posint_negint(self):
        """When power is negative integer and base is positive integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2, -2), pow(2, -2))

    def test_x_power_y_posfloat_posint(self):
        """When power is negative integer and base is positive float value"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2.2, 2), pow(2.2, 2))

    def test_x_power_y_num_string(self):
        """When power is string and base is positive integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2, "string"), "Value Error")

    def test_sin_case_positive(self):
        """test case for sin(30)"""
        calc = ScientificCalc()
        self.assertEqual(calc.sin_func('30'), -0.9880316240928618)

    def test_sin_case3_negative(self):
        """test case for sin(-30)"""
        calc = ScientificCalc()
        self.assertEqual(calc.sin_func('-30'), 0.9880316240928618)

    def test_sin_case3_float(self):
        """test case for sin(30.8)"""
        calc = ScientificCalc()
        self.assertEqual(calc.sin_func('30.8'), -0.5777150444457317)

    def test_sin_case2_exception(self):
        """test case for sin(string)"""
        calc = ScientificCalc()
        self.assertEqual(calc.sin_func('string'), 'Please enter float or integer types input.')

    def test_cube_root(self):
        """test case for check cube root"""
        test = ScientificCalc()
        self.assertEqual(test.cube_root(8), 2)

    def test_cube_root_negative(self):
        """test case for check cube root"""
        test = ScientificCalc()
        self.assertEqual(test.cube_root(-8), -2)

    def test_cube_root1(self):
        """test case for exception"""
        test = ScientificCalc()
        self.assertEqual(test.cube_root("hai"), "ValueError")

    def test_square_root_positive(self):
        """test case for positive value"""
        test = ScientificCalc()
        self.assertEqual(test.square_root(4), 2.0)

    def test_square_root_negative(self):
        """test case for negative value"""
        test = ScientificCalc()
        self.assertEqual(test.square_root(-8), complex(1.7319121124709868e-16 + 2.8284271247461903j))

    def test_square_root_string(self):
        """test case if we give string"""
        test = ScientificCalc()
        self.assertEqual(test.square_root("a"), "expecting integer value")

    def test_rad_zero(self):
        '''check for zero'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad(0), 0)

    def test_rad_positive(self):
        '''check for positive integers'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad(1), 0.017453292519943295)

    def test_rad_negative(self):
        '''check for negative integers'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad(-1), -0.017453292519943295)

    def test_rad_posfloat(self):
        '''check for positive float '''
        calc = ScientificCalc()
        self.assertAlmostEqual(calc.rad(2.5), 0.04363323129985824)

    def test_rad_negfloat(self):
        '''check for negative float'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad(-4.5), -0.07853981633974483)

    def test_rad_string(self):
        '''check for exception'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad("abc"), "Value Error")

    def test_one_by_x_value(self):
        """input=1"""
        calc = ScientificCalc()
        res = calc.one_by_x(1)
        self.assertEqual(res, 1)

    def test_one_by_x_zero_division_error(self):
        """input=0"""
        calc = ScientificCalc()
        self.assertEqual(calc.one_by_x(0), "ZeroDivisionError")

    def test_one_by_x_value_error(self):
        """input=giving string instead of number"""
        calc = ScientificCalc()
        result = calc.one_by_x("s")
        self.assertEqual(result, "ValueError")

    def test_one_by_x_value5(self):
        """when we take 5 as input"""
        calc = ScientificCalc()
        result = calc.one_by_x(5)
        self.assertEqual(result, 0.2)

    def test_positive_angle_values(self):
        """function to test cos 30"""
        scientificcalc = ScientificCalc()
        self.assertEqual(0.15425144988758405, scientificcalc.calculate_cos(30))

    def test_negative_angle_values(self):
        """function to test cos -15"""
        scientificcalc = ScientificCalc()
        self.assertEqual(-0.7596879128588213, scientificcalc.calculate_cos(-15))

    def test_float_angle_values(self):
        """function to test cos 30.5"""
        scientificcalc = ScientificCalc()
        self.assertEqual(0.6090559761063562, scientificcalc.calculate_cos(30.5))

    def test_type_exception(self):
        """function to test cos angle"""
        scientificcalc = ScientificCalc()
        self.assertRaises(TypeError, scientificcalc.calculate_cos('angle'))

    def test_tan_fun_pos(self):
        """function to test against negative input"""
        calc = ScientificCalc()
        self.assertEqual(calc.tan_fun(90), -1.995200412)

    def test_tan_fun_neg(self):
        """function to test against positive input"""
        calc = ScientificCalc()
        self.assertEqual(calc.tan_fun(-90), 1.995200412)

    def test_tan_fun_zero(self):
        """function to test against zero input"""
        calc = ScientificCalc()
        self.assertEqual(calc.tan_fun(0), 0.0)

    def test_tan_fun(self):
        """function to test against random input"""
        calc = ScientificCalc()
        self.assertEqual(calc.tan_fun(56), -0.611273688)

    def test_logarithm(self):
        """test_against_positive_input"""
        res = ScientificCalc()
        self.assertEqual(res.logarithm(100000), 5.0)

    def test_logarithm2(self):
        """test_type_of_variable"""
        res = ScientificCalc()
        self.assertTrue(type(res.logarithm(10)), int)

    def test_logarithm3(self):
        """test_for_negative_number"""
        res = ScientificCalc()
        self.assertEqual(res.logarithm(-10), 'TypeError')

    def test_logarithm4(self):
        """test_for_type_of_variable"""
        res = ScientificCalc()
        self.assertEqual(res.logarithm("prasad"), 'ValueError')

    def test_sinh_30(self):
        """positive value"""
        obj1 = ScientificCalc()
        self.assertEqual(obj1.sine_h(30), 5343237290762.223)

    def test_sinh_neg(self):
        """negative value"""
        obj2 = ScientificCalc()
        self.assertEqual(obj2.sine_h(-1), -1.1752011936438014)

    def test_sinh_0(self):
        """zero"""
        obj3 = ScientificCalc()
        self.assertEqual(obj3.sine_h(0), 0.0)


    def test_for_positive_number(self):
        """test case for checking a Positive number"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(1), 1.5430798443133158)


    def test_for_negative_number(self):
        """test case for checking a Positive number"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(-2), 3.762190811852014)


    def test_for_positive__floating_point_number(self):
        """test case for checking a Positive floating number"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(1.8), 3.1074696140087874)


    def test_for_zero(self):
        """test case for checking for Zero"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(0), 1)


    def test_for_string(self):
        """test case for checking for Zero"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh('fgftgf'), "Value error")

    def test_ln_postive(self):
        """checks for positive value"""
        result = ScientificCalc()
        self.assertEqual(result.ln_func(2), 0.6931471805599453)

    def test_ln_negative(self):
        """checks for negative value"""
        result = ScientificCalc()
        self.assertEqual(result.ln_func(-2), "-NAN-")

    def test_ln_zero(self):
        """checks for zero value"""
        result = ScientificCalc()
        self.assertEqual(result.ln_func(0), "infinity")

    def test_ln_type(self):
        """checks for zero value"""
        result = ScientificCalc()
        self.assertEqual(result.ln_func("ram"), "string is not accepted")

    def test_add_two_positive(self):
        """calculating the two positive addition value"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 2]), 4)

    def test_add_one_negative(self):
        """calculating the one addition and one subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([-2, 4]), 2)

    def test_one_negetive(self):
        """calculating with alternate sign """
        calc = ScientificCalc()
        self.assertEqual(calc.addition([4, -2]), 2)

    def test_add_two_negative(self):
        """calculating two addition value with negative"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([-2, -2]), -4)

    def test_add_multiple_positive(self):
        """calculating the multiple positive addition value"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 2, 3, 4, 5]), 16)

    def test_addition(self):
        """calculating the multiple positive addition value with different sign"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 2, -3, 4, 5]), 10)

    def test_add_alternate_negative(self):
        """calculating the alternate sign positive addition"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, -2, -3, 4, 5]), 6)

    def test_add_floatvalue(self):
        """calculating the float positive addition"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 2.5]), 4.5)

    def test_add_negative_floatvalue(self):
        """calculating the addition value with different sign"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([-2.5, 3.5]), 1)

    def test_error_string_value(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.addition([2, 'a']), "Enter only numbers")

    def test_sub_two_positive(self):
        """calculating the subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([4, 2]), 2)

    def test_sub_one_negative(self):
        """calculating the subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([-2, 4]), -6)

    def test_one_sub_negetive(self):
        """calculating the subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([4, -2]), 6)

    def test_sub_two_negative(self):
        """calculating the two negative subtraction  value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([-7, -2]), -5)

    def test_sub_multiple_positive(self):
        """calculating the multiple subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([2, 2, 3, 4, 5]), -12)

    def test_sub_alternate_negative(self):
        """calculating the multiple subtraction with different sign"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([2, -2, -3, 4, 5]), -2)

    def test_sub_floatvalue(self):
        """calculating the float subtraction  value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([2, 2.5]), -0.5)

    def test_sub_negative_floatvalue(self):
        """calculating the negative float subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([-2.5, 3.5]), -6)

    def test_sub_negative_multiple_floatvalue(self):
        """calculating the multiple float subtraction value"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([-2.5, 3.5, 4.5, 8, -2.7]), -15.8)

    def test_error_sub_string_value(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.subtraction([2, 'a']), "Enter only numbers")

    def test_mul_two_positive(self):
        """calculating the positive multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([4, 2]), 8)

    def test_mul_one_negative(self):
        """calculating the negative multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([-2, 4]), -8)

    def test_mul_two_negative(self):
        """calculating the two negative multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([-7, -2]), 14)

    def test_mul_five_positive(self):
        """calculating the multiple multiplication  value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([2, 2, 3, 4, 5]), 240)

    def test_mul(self):
        """calculating the multiplication value with different sign"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([2, 2, -3, 4, 5]), -240)

    def test_mul_floatvalue(self):
        """calculating the float multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([2, 2.5]), 5)

    def test_mul_negative_floatvalue(self):
        """calculating the negative float multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([-2.5, 3.5]), -8.75)

    def test_mul_negative_multiple_floatvalue(self):
        """calculating the multiple negative float multiplication value"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([-2.5, 3.5, 4.5, 8, -2.7]), 850.5)

    def test_error_mul_string_value(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.multiplication([2, 'a']), "Enter only numbers")

    def test_div_two_positive(self):
        """calculating the positie division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([4, 2]), 2)

    def test_div_one_negative(self):
        """calculating the negative sign division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([-2, 4]), -0.5)

    def test_div_two_negative(self):
        """calculating the two negative sign division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([-7, -2]), 3.5)

    def test_div_multiple_positive(self):
        """calculating the multiple division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 2, 3, 4, 5]), 0.016666666666666666)

    def test_div_negative(self):
        """calculating the negative sign multiple division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 2, -3]), -0.3333333333333333)

    def test_div_floatvalue(self):
        """calculating the float division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 2.5]), 0.8)

    def test_div_negative_floatvalue(self):
        """calculating the negative float division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([-2.5, 3.5]), -0.7142857142857143)

    def test_div_negative_multiple_floatvalue(self):
        """calculating the multiple float division value"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([-2.5, 3.5, 4.5, 8, -2.7]), 0.00734861845972957)

    def test_error_div_string_value(self):
        """non integer inputs"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 'a']), "Enter only numbers")

    def test_zeroerror(self):
        """zero division error"""
        calc = ScientificCalc()
        self.assertEqual(calc.division([2, 0]), "Enter a number greater than zero")
