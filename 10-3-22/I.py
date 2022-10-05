import sys

tokens = (token for token in sys.stdin.read().split()) #generator ??

N = int(next(tokens))
Q = int(next(tokens))

lst = []
for _ in range(N):
    cur_num = int(next(tokens))
    lst.append(cur_num)

def bs(target, min, mid, max):
    if min >= max:
        return -1
    elif target == lst[mid]:
        return mid
    elif target < lst[mid]:
        return bs(target, min, int(mid/2), mid)
    else:
        return bs(target, mid+1, int(mid*1.5), max)
    

for _ in range(Q):
    find = int(next(tokens))
    print(bs(find, 0, int(len(lst)/2), len(lst)))