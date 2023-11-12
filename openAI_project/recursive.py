# 一个简单的递归函数求值器

def recursive_evaluator(func, x):
    """
    Evaluate a recursive function defined by a dictionary.

    :param func: A dictionary defining the recursive function.
    :param x: The input value for which the function should be evaluated.
    :return: The result of the function evaluation.
    """
    if 'base_case_value' in func and x <= func['base_case_limit']:
        return func['base_case_value'](x)
    else:
        return recursive_evaluator(func, x + func['recursive_case_adjustment']) + func['recursive_case_value'](x)

# 定义一个特定的递归函数
recursive_function = {
    'base_case_limit': 0,  # 定义基础情况的限制
    'base_case_value': lambda x: 3 * x,  # 基础情况的函数
    'recursive_case_adjustment': -3,  # 递归调用的参数调整
    'recursive_case_value': lambda x: 1  # 递归情况下要加上的值
}

# 使用递归求值器计算 g(11)
result = recursive_evaluator(recursive_function, 11)
print(result)
