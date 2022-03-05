import math
def get_prime():
    max_val = 10 ** 7 + 1
    print(max_val)
    visit = [False] * max_val

    for i in range(2, max_val):
        if visit[i]: continue
        for j in range(i * i, max_val, i):
            visit[j] = True
    return visit


prime = get_prime()


def get_k(n, k):
    ret = []
    while n > 0:
        n, rem = divmod(n, k)
        ret.append(rem)
    ret.reverse()
    return ''.join(map(str, ret))


def solution(n, k):
    answer = 0
    max_val = 10 ** 7 + 1
    s = get_k(n, k)
    #s = '1111111'
    ary = s.split('0')
    for ele in ary:
        if not ele: continue
        val = int(ele)
        if 1<val<max_val and not prime[val]:
            answer += 1
        elif val > max_val:
            sq_val = int(math.sqrt(val))
            flag = True
            for i in range(2, sq_val+1):
                if val % i == 0:
                    flag = False
                    break
            if flag: answer += 1

    return answer

print(solution(110011,10))