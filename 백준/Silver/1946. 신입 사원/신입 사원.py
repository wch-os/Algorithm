import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

T = int(input()) # 테스트케이스 개수

# (1등, a) / (b, 1등)
def solve(start, end):
    global count

    for i in range(start+1, N+1): # N명 모두 등수가 낮은 지원자부터 탐색
        # 등수 내의 지원자가 있을 시 count
        if i < b and rank[i] < end:
            count += 1
            solve(i, rank[i]) # 위 지원자를 포함해서, 범위를 재계산해서 재귀
            break # 그 뒤의 지원자는 볼 필요 없음
    return

for _ in range(T):
    N = int(input()) # 지원자 숫자

    count = 0
    veryGood = False # (1등, 1등)인 지원자

    rank = {}
    for _ in range(N):
        s1, s2 = map(int, input().split())
        if s1 == 1 and s2 == 1:
            veryGood = True
        elif s1 == 1: #서류 1등, 면접 a등
            a = s2
        elif s2 == 1: #서류 b등, 면접 1등
            b = s1

        rank[s1] = s2

    if veryGood:
        print(1)
    else:
        solve(1, a)
        print(count+2)