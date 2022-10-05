import sys

tokens = (token for token in sys.stdin.read().split()) #generator ??

N = int(next(tokens))
K = int(next(tokens))

lst = []
for _ in range(N):
    cur_num = int(next(tokens))
    lst.append(cur_num)

sum = 0
for i in range(0, K):
    sum += lst[i]

minheight = sum
minindex = 0

for i in range(1, len(lst) - K + 1):
    sum = 0
    for x in range(i, i + K):
        sum += lst[x]
    if sum < minheight:
        minheight = sum
        minindex = i

print(minindex + 1)