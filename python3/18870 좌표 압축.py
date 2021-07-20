import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))

dic = {}
nums = list(set(ary))
nums.sort()

for i in range(len(nums)):
    dic[nums[i]] = i

ary = [dic[x] for x in ary]
print(' '.join(map(str, ary)))