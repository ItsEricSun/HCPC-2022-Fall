import sys
N = int(sys.stdin.read())
accepted = []

for i in range(1, 101):
    for c in range(0, 25):
        for d in range(0, 14):
            if 4*c + 7*d == i: 
                accepted.append(i)
                break

if N in accepted: print("Yes")
else: print("No")