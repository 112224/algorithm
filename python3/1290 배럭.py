input = __import__('sys').stdin.readline

n,b,u = map(int, input().split())
enemy = 0

def no_barrack(m1, m2, can_attack = 0, opt = False):
    cnt = 0
    while m1 > 0 and m2 > 0:
        if can_attack:
            m2 -= can_attack
            can_attack = 0
        else:
            m2 -= m1
        m1 -= m2
        cnt += 1
    if not opt:
        return m1 <= 0
    else:
        return m1 <= 0, cnt
# 배럭을 빨리 부시고 마린을 다 죽이려면?
# 일정 이상 동안은 생산되는 마린 만큼 죽이고, 나머지는 배럭 공격하는게 젤 빠름
# n + t(n-u)
# 25 +t(25 - 10) = 25 + 15* 11 = 10(12일) 10 + 10 - 25 (1일)
# case 1 배럭피 + 생성된 마린 < 내 마린    => 하루 더 하면 끗
# 10 + t(10 - 15) = 10 +   1 + 15 > 10
# 배럭피 + 생성된 마린 > 내 마린     => 일단 배럭피 까고 나머지 마린 죽여보자
for ans in range(1, 5011):
    b -= (n - enemy)
    # 첫날 펑 아니면 여기서 못걸림
    if b <= 0:
        break
    enemy = u
    # 여기가 한 턴 끗
    if b < n and not no_barrack(n, enemy, can_attack= n - b):
        break
# 배럭을 부실 수 있어야 함 못부시면 에러,
# ans < 5000 why? 배럭 피 최소 1씩은 달아야 함 + 첫 날은 한대 이상
# u > n and b > n 인데 터트리기 가능?
# => 첫날 쏘고나서 결정 만약 2일 이상 배럭이 안깨지면? 불가능
# 역시 틀
# print(ans, n, b, enemy)
if ans == 5010:
    print(-1)
else:
    flag, cnt = no_barrack(n, enemy, can_attack=n - b if b > 0 else 0,opt=True)
    if not flag:
        print(ans + cnt)