# print("Hello", end='')
# print("world", end='')

print("Hello\tWorld")
print("itheima\tbest")
for i in range(1, 10):
    print(i, end="\n")
    for j in (0, i, 1):
        print(j, end="\t")
    print()

n = int(input())
jishu = 0
oushu = 0
jiecheng = 1
for i in range(1, n,1):
    if i % 2 == 0:
        oushu += 1

    else:
        jishu += 1
    jiecheng *= i
print(jishu, oushu, jiecheng)

def sum_of_odd_numbers(n):
    return n * (n - 1)

if __name__ == "__main__":
    n = int(input())
    result = sum_of_odd_numbers(n)
    print(result)
