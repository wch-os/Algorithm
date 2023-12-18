# 인용 코드

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
parties = [list(map(int,input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if parties[i][j] > parties[i][k] + parties[k][j]:
                parties[i][j] = parties[i][k] + parties[k][j]
for _ in range(M):
    A, B, C = map(int,input().split())
    if parties[A-1][B-1] <= C:
        print('Enjoy other party')
    else:
        print('Stay here')