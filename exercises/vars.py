# a fn named print calc result that takes in array of values and operator
# and prints the result of the operation

def print_calc_result(values, operator):
    result = 0
    for value in values:
        if operator == '+':
            result += value
        elif operator == '-':
            result -= value
        elif operator == '*':
            result *= value
        elif operator == '/':
            result /= value
    return result