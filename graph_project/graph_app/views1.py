import cv2
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse

def upload_graph(request):
    if request.method == 'POST' and request.FILES['graph_image']:
        image_file = request.FILES['graph_image'].read()
        image_nparray = np.frombuffer(image_file, np.uint8)
        image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

        # 转换为灰度图像
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # 使用Hough变换检测圆形节点
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=30, minRadius=25, maxRadius=50)
        
        if circles is not None:
            circles = np.uint16(np.around(circles))
            num_nodes = circles.shape[1]
            adjacency_matrix = np.zeros((num_nodes, num_nodes))

            # 检测边
            edges = cv2.Canny(gray, 100, 200)
            
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if i != j:
                        # 检查两个节点之间是否存在边
                        x1, y1, _ = circles[0][i]
                        x2, y2, _ = circles[0][j]
                        line_points = cv2.line(np.zeros_like(edges), (x1, y1), (x2, y2), 1, 2)
                        if np.any(np.logical_and(edges, line_points)):
                            adjacency_matrix[i][j] = 1

            # 将邻接矩阵返回给浏览器
            return JsonResponse({'adjacency_matrix': adjacency_matrix.tolist()})

    return render(request, 'graph_app/upload_graph.html')
