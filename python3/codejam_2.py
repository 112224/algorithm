from copy import deepcopy
def solve():
    tc = int(input())

    req = 10**6
    for test_case in range(tc):
        printer = [list(map(int, input().split())) for _ in range(3)]
        mins = [min(printer[0][j], printer[1][j], printer[2][j]) for j in range(4)]

        sums = sum(mins)
        answer = None
        if sums < req:
            answer = 'IMPOSSIBLE'
        else:
            diff = sums - req
            for i in range(4):
                if mins[i] >= diff:
                    mins[i] -= diff
                    break
                else:
                    diff -= mins[i]
                    mins[i] = 0
            answer = ' '.join(map(str, mins))
        print(f'Case #{test_case + 1}: {answer}')


solve()

