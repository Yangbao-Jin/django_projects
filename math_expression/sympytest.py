import pyeda.inter as pyeda
from graphviz import Digraph

# 输入布尔表达式
boolean_expression = input("请输入布尔表达式（使用与、或、非和括号）：")

# 解析布尔表达式
expr = pyeda.expr(boolean_expression)

# 创建Graphviz Digraph对象
dot = Digraph(comment="Boolean Circuit")

# 递归生成门电路图
def generate_circuit(dot, expression):
    if isinstance(expression, pyeda.boolalg.OrOp):
        dot.node(str(id(expression)), 'OR')
        for i, arg in enumerate(expression.args):
            dot.edge(str(id(expression)), str(id(arg)), label=f'Input {i+1}')
            generate_circuit(dot, arg)
    elif isinstance(expression, pyeda.boolalg.AndOp):
        dot.node(str(id(expression)), 'AND')
        for i, arg in enumerate(expression.args):
            dot.edge(str(id(expression)), str(id(arg)), label=f'Input {i+1}')
            generate_circuit(dot, arg)
    elif isinstance(expression, pyeda.boolalg.NotOp):
        dot.node(str(id(expression)), 'NOT')
        dot.edge(str(id(expression)), str(id(expression[0])), label='Input')
        generate_circuit(dot, expression[0])
    else:
        dot.node(str(id(expression)), str(expression))

# 生成门电路图
generate_circuit(dot, expr)

# 保存门电路图到文件（可选）
dot.render('boolean_circuit', view=True)
