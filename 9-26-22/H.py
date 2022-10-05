import sys

tokens = (token for token in sys.stdin.read().split())

N = int(next(tokens))

lst = []
for _ in range(N):
    cur_num = int(next(tokens))
    lst.append(cur_num)

for i in range(0,len(lst)):
    if i == 0:
        mi = abs(lst[0] - lst[1])
        ma = abs(lst[0] - lst[len(lst) - 1])
    elif i == len(lst) - 1:
        mi = abs(lst[i] - lst[i - 1])
        ma = abs(lst[0] - lst[i])
    else:
        mi = min(abs(lst[i] - lst[i-1]), abs(lst[i] - lst[i+1]))
        ma = max(abs(lst[i] - lst[0]), abs(lst[i] - lst[len(lst) - 1]))
    print(str(mi) + " " + str(ma))