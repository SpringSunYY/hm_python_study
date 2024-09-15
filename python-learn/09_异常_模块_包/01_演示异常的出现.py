"""
主动写一段错误代码，演示异常的出现
"""

# 通过open，读取一个不存在的文件
try:
    f = open("D:/abc.txt", "r", encoding="UTF-8")
except Exception as e:
    print(f"出错了:{e}")
