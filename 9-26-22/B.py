import sys
N = int(sys.stdin.read())
while(True):
    if(N % 4 == 2):
        print(N)
        break
    else: N += 1