import sys

tokens = (token for token in sys.stdin.read().split()) 

N = int(next(tokens))

lst = []
for _ in range(N):
    x = int(next(tokens))
    y = int(next(tokens))
    n = int(next(tokens))
    lst.append((x, y, n))

# for x, y, n in lst:
#     for i in range(n, -1, -1):
#         if i % x == y: 
#             print(i)
#             break



# # print(12345%7)

for x, y, n in lst:
    c = n % x
    if c < y:
        n = n + y - c
        print(n - x)
    else:
        print(n + y - c)