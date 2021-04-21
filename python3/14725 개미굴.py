import sys
input = sys.stdin.readline
#print = sys.stdout.write

class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, ary):
        cur = self.root
        for ele in ary:
            if ele not in cur:
                cur[ele] = {}
            cur = cur[ele]
        cur[0] = True

    def prints(self, depth, cur):
        if 0 in cur:
            return
        cur_children = sorted(cur)
        for child in cur_children:
            print("--"*depth + child)
            self.prints(depth+1, cur[child])

n = int(input())
nest = Trie()
for _ in range(n):
    ary = input().split()
    nest.insert(ary[1:])

nest.prints(0, nest.root)
