input = __import__('sys').stdin.readline

n = int(input())

def solution(n):
    squares = []
    for i in range(1, n+1):
        val = i**2
        if val == n:
            return 1
        if val > n:
            break
        squares.append(val)

    for i in squares:
        if n - i in squares:
            return 2

    for i in squares:
        ns = n - i
        for j in squares:
            val = ns - j
            if val in squares:
                return 3
            if val < 0:
                break
    return 4
print(solution(n))