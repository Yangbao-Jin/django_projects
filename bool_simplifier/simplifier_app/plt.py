import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_and_gate(x, y):
    # 绘制AND门
    plt.plot([x, x+0.5], [y+0.2, y+0.2], color='black')  # 输入线1
    plt.plot([x, x+0.5], [y-0.2, y-0.2], color='black')  # 输入线2
    plt.plot([x+1.5, x+2], [y, y], color='black')        # 输出线
    plt.gca().add_patch(patches.Rectangle((x+0.5, y-0.5), 1, 1, fill=False))  # 矩形
    plt.gca().add_patch(patches.Arc((x+1.5, y), 1, 1, theta1=-90, theta2=90))  # 半圆

def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()

    draw_and_gate(1, 1)
    plt.show()

main()
