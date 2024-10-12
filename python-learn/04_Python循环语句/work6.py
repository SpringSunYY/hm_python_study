# 定义正确的用户名和密码
correct_username = "seven"
correct_password = "123"

# 初始化错误计数
attempts = 0


# while attempts < 3:
#     username = input("请输入用户名: ")
#     password = input("请输入密码: ")
#
#     if username == correct_username and password == correct_password:
#         print("登陆成功")
#         break
#     else:
#         print("登陆失败")
#         attempts += 1
#
# if attempts == 3:
#     print("登陆失败次数达到三次")

def is_prime(num):
    """判断一个数字是否为质数"""
    if num < 2:
        return False  # 质数必须大于1
    for i in range(2, num):  # 从2到num-1检查是否能整除
        if num % i == 0:
            return False  # 找到因数，返回False
    return True  # 没有因数，返回True


def print_primes(n):
    """打印 n 以内的所有质数"""
    primes = [str(i) for i in range(2, n) if is_prime(i)]  # 生成质数列表
    print(" ".join(primes))  # 用空格连接质数并打印


# 获取用户输入
n = int(input("请输入一个正整数: "))  # 提示用户输入正整数
print_primes(n)  # 打印 n 以内的质数

for i in range(2, n):
    bol = True
    for j in range(2, i):
        if i % j == 0:
            bol = False
            break
    if bol:
        print(i)
# import math
#
# # 输入下限和上限
# a = float(input("请输入下限 a: "))
# b = float(input("请输入上限 b: "))
#
# # 将下限和上限放大1000倍
# a_mul_1000 = int(a * 1000)
# b_mul_1000 = int(b * 1000)
#
# # 初始化积分结果
# s = 0.0
#
# # 使用放大后的范围进行循环
# for x in range(a_mul_1000, b_mul_1000):
#     # 将 x 除以 1000 转换为实际值，并计算 sin(x)
#     s += math.sin(x / 1000)
#
# # 乘以步长（1/1000）来得到最终结果
# s *= 1 / 1000
#
# # 输出结果，保留小数点后两位
# print(round(s, 2))
