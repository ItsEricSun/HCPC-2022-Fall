import sys

tokens = (token for token in sys.stdin.read().split())

N = int(next(tokens))

(next(tokens))

lst = []
for _ in range(N):
    cur_num = (next(tokens))
    lst.append(cur_num)

for x in lst:
    print(x)
    print(x)
