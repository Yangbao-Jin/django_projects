import math

# 检查一个数是否是完全平方数
def is_perfect_square(n):
    return n == math.isqrt(n) ** 2

# 寻找满足条件的y值
def find_y():
    y = 1
    while True:
        # 计算对应的x的平方
        potential_square = y**2 + 23*y + 100
        # 检查是否为完全平方数
        if is_perfect_square(potential_square):
            x = math.isqrt(potential_square) - 10
            # 检查x是否为整数
            if x == int(x):
                return x, y
        y += 1

# 计算N的各位数之和
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# 主程序
def main():
    x, y = find_y()
    N = x * (x + 20)  # 或者 y * (y + 23), 结果应该相同
    print(f"找到的x值为: {x}")
    print(f"找到的y值为: {y}")
    print(f"N的值为: {N}")
    print(f"N的各位数之和为: {sum_of_digits(N)}")

# 运行主程序
main()
