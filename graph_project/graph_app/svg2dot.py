import xml.etree.ElementTree as ET

def svg_to_dot(svg_filename):
    tree = ET.parse(svg_filename)
    root = tree.getroot()

    nodes = {}
    edges = []

    # 提取圆形元素作为节点
    for circle in root.findall(".//{http://www.w3.org/2000/svg}circle"):
        cx = float(circle.get('cx'))
        cy = float(circle.get('cy'))
        nodes[(cx, cy)] = ""
        print(f"Found circle at ({cx}, {cy})")

    # 提取圆形中的字母作为节点名
    for text in root.findall(".//{http://www.w3.org/2000/svg}text"):
        x = float(text.get('x'))
        y = float(text.get('y'))
        node_name = text.text
        nodes[(x, y)] = node_name
        print(f"Found text '{node_name}' at ({x}, {y})")

    # 提取线条元素作为边
    for line in root.findall(".//{http://www.w3.org/2000/svg}line"):
        x1, y1 = float(line.get('x1')), float(line.get('y1'))
        x2, y2 = float(line.get('x2')), float(line.get('y2'))
        source = nodes.get((x1, y1), None)
        target = nodes.get((x2, y2), None)
        if source and target:
            edges.append((source, target))
            print(f"Found edge from {source} to {target}")

    # 生成 DOT 语法
    dot_syntax = "digraph G {\n"
    for node, name in nodes.items():
        if name:
            dot_syntax += f"    {name};\n"
    for edge in edges:
        dot_syntax += f"    {edge[0]} -> {edge[1]};\n"
    dot_syntax += "}"

    return dot_syntax

# 使用示例


svg_filename = "graph2.svg"  # 替换为您的SVG文件名
print(svg_to_dot(svg_filename))
