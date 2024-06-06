# 풀이 시간: 35분
# 시간복잡도: O(N^N)
# 공간복잡도: O(N)
# 유형: backtracking
# 참고: 


result = 0
def dfs(start):
    global result

    if start == N:
        cnt = len([x[0] for x in eggs if x[0] <= 0])
        result = max(result, cnt)
        return


    broken = False
    for i in range(N):
        # 현재 계란이 깨져있을 때
        if eggs[start][0] <= 0:
            dfs(start + 1)

        # 내구도 O
        elif eggs[i][0] > 0:
            if i == start: # 같은 계란일 경우
                continue

            broken = True
            eggs[start][0] -= eggs[i][1]
            eggs[i][0] -= eggs[start][1]

            dfs(start + 1)

            eggs[start][0] += eggs[i][1]
            eggs[i][0] += eggs[start][1]

    # 계란이 모두 깨져, 하나도 못 깨트렸을 때
    if not broken:
        dfs(start + 1)



N = int(input())

eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split())))

dfs(0)
print(result)
