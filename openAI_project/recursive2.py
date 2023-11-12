# 一个递归函数求值器，可以处理多个分支条件

def recursive_evaluator(x, rules):
    """
    Evaluate a recursive function with multiple branches.

    :param x: The input value for which the function should be evaluated.
    :param rules: A list of tuples defining the recursive function branches.
                  Each tuple contains a condition function and a result function.
    :return: The result of the function evaluation.
    """
    for condition, result in rules:
        if condition(x):
            return result(x)

# 定义递归函数的不同分支条件及其结果
recursive_rules = [
    # 当 x > 5 时
    (lambda x: x > 5, lambda x: recursive_evaluator(x - 7, recursive_rules) + 1),
    # 当 0 <= x <= 5 时
    (lambda x: 0 <= x <= 5, lambda x: x),
    # 当 x < 0 时
    (lambda x: x < 0, lambda x: recursive_evaluator(x + 3, recursive_rules))
]

# 使用递归求值器计算 h(x) 的值
result = recursive_evaluator(13, recursive_rules)
print(result)
