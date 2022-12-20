import model_rational_numbers
import model_complex
import view

def calc():
    mode = view.get_mode()
    num1, sign, num2 = view.get_data()
    if mode == 1:
        result = model_rational_numbers.calc_value(num1, num2, sign)
    else:
        result = model_complex.calc_value(num1, num2, sign)
    view.view_data(result)