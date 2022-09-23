from collections import deque

def solution(queue1, queue2):
    cnt = 0

    s1, s2 = sum(queue1), sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)

    max_cnt = len(q1) + len(q2)

    while s1 != s2 and cnt < max_cnt * 2 + 1:
        if s1 < s2:
            val = q2.popleft()
            s2 -= val
            s1 += val
            q1.append(val)
        else:
            val = q1.popleft()
            s1 -= val
            s2 += val
            q2.append(val)
        cnt += 1

    return cnt if s1 == s2 else -1

print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]))