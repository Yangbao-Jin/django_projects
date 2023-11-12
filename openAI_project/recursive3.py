# 递归函数求值器，可以处理多个分支条件和双参数

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

# 定义递归函数的不同分支条件及其结果
recursive_rules = [
    # 当 x > y 时
    (lambda x, y: x > y, lambda x, y: recursive_double_evaluator(x - y, y - 1, recursive_rules) + 2),
    # 否则（x <= y）
    (lambda x, y: x <= y, lambda x, y: x + y)
]

# 使用递归求值器计算 f(x, y) 的值
result = recursive_double_evaluator(12, 6, recursive_rules)
print(result)
