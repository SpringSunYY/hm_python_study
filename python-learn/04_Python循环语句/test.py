# print("Hello", end='')
# print("world", end='')

print("Hello\tWorld")
print("itheima\tbest")
for i in range(1, 10):
    print(i, end="\n")
    for j in (0, i, 1):
        print(j, end="\t")
    print()