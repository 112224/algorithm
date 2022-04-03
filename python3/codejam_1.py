from copy import deepcopy
def solve():
    tc = int(input())
    base = [['..+'],['..|'],['+-+']]
    add_col = [['-+'], ['.|'], ['-+']]
    add_row = [['|.|'], ['+-+']]
    for test_case in range(tc):
        r, c = map(int, input().split())
        answer = []
        for i in range(r):
            tmp = deepcopy(base) if i == 0 else deepcopy(add_row)
            for j in range(1, c):
                val = 3 if i == 0 else 2
                diff = 3 - val
                for k in range(val):
                    tmp[k] += add_col[k+diff]
            answer.extend(tmp)
        print(f'Case #{test_case + 1}:')
        for ele in answer:
            print(''.join(ele))

solve()

