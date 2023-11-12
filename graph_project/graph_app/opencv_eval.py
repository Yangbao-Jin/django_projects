import cv2
import numpy as np

def detect_nodes_edges(image_path):
    # 读取图片并转换为灰度图
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 使用Hough变换检测圆形
    circles = cv2.HoughCircles(
        gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30, param1=50, param2=30, minRadius=5, maxRadius=30)

    nodes = []
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            nodes.append((x, y))

    # 使用Canny检测边缘
    edges_image = cv2.Canny(gray, 50, 150)

    # 使用Hough变换检测直线
    lines = cv2.HoughLines(edges_image, 1, np.pi / 180, 100)
    edges = []

    if lines is not None:
        for line in lines:
            for rho, theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))

                edges.append(((x1, y1), (x2, y2)))

    return nodes, edges

def build_adjacency_matrix(nodes, edges):
    n = len(nodes)
    matrix = np.zeros((n, n))

    for edge in edges:
        start, end = edge
        start_idx = find_closest_node(start, nodes)
        end_idx = find_closest_node(end, nodes)
        matrix[start_idx][end_idx] = 1
        matrix[end_idx][start_idx] = 1  # Assuming undirected graph

    return matrix

def find_closest_node(point, nodes):
    x, y = point
    distances = [(idx, np.sqrt((x - nx)**2 + (y - ny)**2)) for idx, (nx, ny) in enumerate(nodes)]
    distances.sort(key=lambda item: item[1])
    return distances[0][0]

if __name__ == "__main__":
    image_path = 'graph2.png'
    nodes, edges = detect_nodes_edges(image_path)
    matrix = build_adjacency_matrix(nodes, edges)
    print(matrix)
