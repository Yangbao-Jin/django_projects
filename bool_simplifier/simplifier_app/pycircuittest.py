from pycircuit.circuit import Node, Resistor, Circuit
import pycircuit.formats

# 创建电路节点
n1 = Node("N1")
n2 = Node("N2")
gnd = Node("GND")

# 创建电阻
r1 = Resistor(n1, n2, 1000)  # 1k ohm
r2 = Resistor(n2, gnd, 2000)  # 2k ohm

# 创建电路
circuit = Circuit([n1, n2, gnd], [r1, r2])

# 绘制电路图
circuit.draw()
