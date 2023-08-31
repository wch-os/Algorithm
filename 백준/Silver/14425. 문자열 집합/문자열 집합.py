import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N개의 문자열, M개의 문자열

dict = {}
count = 0

for _ in range(N):
    dict[input()] = 1 # input 받은 string을 key 값으로 사전에 저장

for _ in range(M):
    s = input()

    if s in dict: # 사전에 있는 값이면 count++
        count += 1

print(count)