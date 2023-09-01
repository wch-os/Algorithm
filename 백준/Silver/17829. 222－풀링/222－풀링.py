N = int(input()) # N개의 줄, 각 행의 원소 갯수
ary = [list(map(int, input().split())) for _ in range(N)]

def solve(i, j, N):
    result = []

    # 2*2 크기가 되면, 스탑
    if N == 2:
        # 4칸에 있는 숫자 저장하기
        lst = [ary[i][j], ary[i + 1][j], ary[i][j + 1], ary[i + 1][j + 1]]

        # 2번째로 큰 숫자 return
        lst.sort()
        return lst[-2]

    mid = N//2
    result.append(solve(i, j, N//2)) # 1사분면
    result.append(solve(i, mid + j,N//2)) # 2사분면
    result.append(solve(mid + i, j, N//2)) # 3사분면
    result.append(solve(mid + i,mid + j, N//2)) # 4사분면

    result.sort()
    return result[-2]

print(solve(0, 0, N))