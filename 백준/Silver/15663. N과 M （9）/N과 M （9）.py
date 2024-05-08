# 풀이 시간 : 20분 + 15분
# 시간복잡도 : O(nP2)
# 공간복잡도 : O(N)
# 참고 : https://velog.io/@rkdalstn7221/%EB%B0%B1%EC%A4%80-15663N%EA%B3%BC-M9-Python

# 일단 손으로 끄적이자;;
# mlist가 중복된 것인지 판단과, deepcopy에서 시간초과 난 듯

# visited[]로 m개의 숫자로 몇번째 위치에 있는 수를 사용하는지 확인하고
# duplicated로 중복된 수를 걸러준다.
    # 정렬을 했으므로 직전 값과 같은지만 확인해 주면 됨


def backtracking():
    if len(mlist) == M:
        print(*mlist)
        return

    duplicated = 0
    for i in range(N):
        if not visited[i]:  # 해당 위치에 있는 수를 사용했는지
            if lst[i] != duplicated: # 중복된 수가 있는지 (9, 9)
                visited[i] = True
                mlist.append(lst[i])

                duplicated = lst[i]
                backtracking()

                visited[i] = False
                mlist.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = []
mlist = []
visited = [False] * N
backtracking()