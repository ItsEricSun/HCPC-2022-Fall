import sys

tokens = (token for token in sys.stdin.read().split())

N = int(next(tokens))

lst = []
for _ in range(N):
    cur_num = int(next(tokens))
    lst.append(cur_num)

t = 0

for x in lst:
    if x <= 10: continue
    else: t += (x - 10)

print(t)