num = int(input())

a = num // 10
b = num % 10

if a and a % 3 == 0:
    print('clap!', end=' ')
if b and b % 3 == 0:
    print('clap!')