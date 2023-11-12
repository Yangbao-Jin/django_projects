import matplotlib.pyplot as plt
import networkx as nx

# 创建一个空的有向图
G = nx.DiGraph()

# 添加节点
G.add_nodes_from(['A', 'B', 'C', 'D'])

# 根据邻接矩阵添加边
edges = [('A', 'B'), ('A', 'D'), 
         ('B', 'A'), ('B', 'C'), ('B', 'D'), 
         ('C', 'A'), 
         ('D', 'B'), ('D', 'C')]

G.add_edges_from(edges)

# 画图
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1200)
plt.show()