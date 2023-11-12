import re

def parse_condition(condition_str):
    """
    Parse the condition part of a rule.
    
    :param condition_str: The condition part as a string.
    :return: A lambda function representing the condition.
    """
    if condition_str == 'otherwise':
        return lambda x, y: True
    # No need to replace 'x' and 'y' with '{}', as we can directly use them in the lambda
    return eval(f"lambda x, y: {condition_str}")


def parse_result(result_str):
    """
    Parse the result part of a rule.
    
    :param result_str: The result part as a string.
    :return: A lambda function representing the result calculation.
    """
    # This pattern will match all recursive calls
    pattern = re.compile(r'f\(([^)]+)\)')
    
    # This function will be called for each match
    def replace_with_lambda(match):
        args = match.group(1)
        return f"recursive_double_evaluator({args}, rules)"
    
    # Replace all f(...) with the appropriate lambda calls
    result_str = pattern.sub(replace_with_lambda, result_str)
    # Replace arithmetic operations involving 'x' and 'y' with '{}'
    result_str = result_str.replace('x', '{}').replace('y', '{}')
    # Wrap everything in an eval to evaluate arithmetic expressions
    return eval(f"lambda x, y, rules: {result_str.format('x', 'y')}")

def equation_to_rules(equation_str):
    """
    Convert an equation string into a list of rules.
    
    :param equation_str: The entire equation as a string.
    :return: A list of rules, where each rule is a tuple (condition, result).
    """
    rules = []
    # Split the string into separate lines for each rule
    for line in equation_str.strip().split('\n'):
        if 'otherwise' in line:
            # Handle the 'otherwise' case without a condition
            result_str = line.split('=')[1].strip()  # Get the result part
            condition = lambda x, y: True  # Always true condition
            result = parse_result(result_str)
        else:
            condition_str, result_str = line.split(' when ')
            condition = parse_condition(condition_str.split('=')[1].strip())
            result = parse_result(result_str.strip())
        rules.append((condition, result))
    return rules



def recursive_double_evaluator(x, y, rules):
    """
    Evaluate a double-parameter recursive function with multiple branches.

    :param x: The first input value for the function.
    :param y: The second input value for the function.
    :param rules: A list of tuples defining the recursive function branches.
                  Each tuple contains a condition function and a result function.
    :return: The result of the function evaluation.
    """
    for condition, result in rules:
        if condition(x, y):
            return result(x, y)
# Example equation string
equation_str = """
f(x,y)=f(x-y, y-1)+2 when x>y
f(x,y)=x+y otherwise
"""

# Convert the equation string into rules
recursive_rules = equation_to_rules(equation_str)

# The rest of the recursive_double_evaluator definition is as before...
# Now you can use the recursive_rules to evaluate the function
result = recursive_double_evaluator(12, 6, recursive_rules)
print(f"f(12, 6) = {result}")
