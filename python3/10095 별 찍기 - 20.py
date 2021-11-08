n = int(input())
str1 = '* ' * n
str2 = ' *' * n

for i in range(n):
    print(str2 if i % 2 else str1)