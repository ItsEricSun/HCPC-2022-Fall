import sys

tokens = (token for token in sys.stdin.read().split()) #generator ??

N = int(next(tokens))
Q = int(next(tokens))

lst = []
for _ in range(N):
    cur_num = int(next(tokens))
    lst.append(cur_num)

queries = []
for _ in range(Q):
    left_index = int(next(tokens))
    right_index = int(next(tokens))
    queries.append((left_index, right_index))



for left_index, right_index in queries:
    a = 0
    b = 0
    c = 0
    for x in range(left_index - 1, right_index):
        number = lst[x]
        if number == 1:
            a += 1
        elif number == 2:
            b += 1
        else:
            c += 1
    print(str(a) + " " + str(b) + " " + str(c))

    