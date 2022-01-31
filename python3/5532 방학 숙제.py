L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

a1, b1 = A // C, B//D
print(L - max(a1 if A%C == 0 else a1 + 1, b1 if B%D ==0 else b1 + 1))