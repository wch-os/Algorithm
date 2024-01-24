# 구현

# 풀이 시간 : 30분
# 시간복잡도 : O(M * a)
# 공간복잡도 : O(M or N)
# 참고 : -

# 맨 처음에 제시한 사람은 무조건 "진실"만을 들어야 한다.
# 각 사람마다 일관되게 "과장된 이야기 or 진실"을 들어야 한다.
# 해당 파티에서는 무조건 "과장된 이야기 or 진실"을 이야기해야 한다.

# 제시한 사람이 있는 파티는 일단 전부 진실을 말한다.
# 위 파티에 있는 사람들 모두 "진실파티" 에 넣는다.
# 각 파티를 탐색하면서 파티 참석 인원 중
    # "진실파티"에 있는 사람이 있다면
        # 해당 파티에서는 무조건 진실만을 말해야 한다.
        # "진실파티"에 추가를 하고, 파티를 다시 탐색해야 한다.
    # 없다면 해당 루프에서 종료한다.

import sys
input = sys.stdin.readline

# 사람의 수, 파티의 수
N, M = map(int, input().split())

# 진실을 아는 사람의 수, 번호가 주어짐
knowList = list(map(int, input().split()))
knowList.remove(knowList[0])
knowList = set(knowList)

# 각 파티에 오는 사람의 수, 번호
partyList = [list(map(int, input().split())) for _ in range(M)]

# 각 파티에서 거짓말을 할 수 있는지를 체크할 수 있는 리스트
# True : 거짓말 가능 / False : 진실만을 말함
visitedLie = [False] * M

while True:
    knowListLength = len(knowList)

    # 모든 파티 탐색
    for i in range(M):
        addTrue = False
        # 각 파티에 "진실 파티원"이 있는지 탐색
        for j in range(1, len(partyList[i])):
            # "진실 파티원"이 있을 경우 "진실파티"에 추가
            if partyList[i][j] in knowList:
                for k in range(1, len(partyList[i])):
                    knowList.add(partyList[i][k])
                addTrue = True
                break

        # 추가되었음을 flag → 해당 파티에서는 진실만을 말해야한다.
        if addTrue:
            visitedLie[i] = False

        # "진실 파티원"이 없기 때문에 해당 파티에서는 거짓말을 말해도 된다.
        else:
            visitedLie[i] = True

    # 모든 파티를 탐색했음에도 더 이상 "진실파티"가 갱신이 되지 않는 경우 탐색을 종료한다.
    if knowListLength == len(knowList):
        break


# 거짓말을 해도 되는 파티 개수를 출력한다.
result = 0
for i in range(M):
    if visitedLie[i]:
        result += 1

print(result)