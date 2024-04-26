import sys
input = sys.stdin.readline

N = int(input())

a, b = 0, 0
for _ in range(N):
    s = int(input())

    if s:
        a += 1
    else:
        b += 1

        
if a > b:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")