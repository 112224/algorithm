input = __import__('sys').stdin.readline

def solve():
    n = int(input())
    ary = list(map(int, input().split()))
    b, c = map(int, input().split())

    ret = 0
    for ele in ary:
        ele -= b
        ret += 1
        if ele > 0:
            val, rem = divmod(ele, c)
            val = val if rem == 0 else val + 1
            ret += val
    return ret

print(solve())