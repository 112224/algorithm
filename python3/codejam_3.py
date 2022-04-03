input = __import__('sys').stdin.readline
def solve():
    tc = int(input())
    for test_case in range(tc):
        n = int(input())
        ary = list(map(int, input().split()))
        ary.sort()
        answer = 1
        for ele in ary:
            if ele >= answer:
                answer += 1
        answer -= 1
        print(f'Case #{test_case + 1}: {answer}')

solve()

