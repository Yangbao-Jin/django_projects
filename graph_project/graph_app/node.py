import cv2
import numpy as np

# 读取图像
image = cv2.imread('graph4.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 显示灰度图像
cv2.imshow('Gray Image', gray)
cv2.waitKey(0)

# 使用Canny边缘检测
edges = cv2.Canny(gray, 50, 150)

# 显示Canny结果
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)

# 查找轮廓
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours):
    # 创建一个全黑的背景图像
  
    
    # 在黑色背景上绘制当前轮廓，颜色设置为白色
    
    
    # 显示轮廓
 
    # 计算轮廓的面积和周长
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    
    # 圆形度
    if perimeter == 0:
        continue
    circularity = 4 * np.pi * area / (perimeter * perimeter)
    
    # 如果轮廓的圆形度接近1，我们可以认为它是一个圆
    if 0.5 < circularity < 1.3:
        # 获取该轮廓的边界矩形
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

