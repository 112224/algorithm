def solution(n, start, end, roads, traps):
    answer = 0
    m = len(traps)
    val = (1 << m) - 1
    print(val)
    return answer

print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2, 3]))