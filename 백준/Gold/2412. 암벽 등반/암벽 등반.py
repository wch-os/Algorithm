# 풀이 시간 : 40분 + 30분
# 시간복잡도 : O(n^2), bfs 시간복잡도
# 공간복잡도 : O(n)
# 참고 : https://lagooni.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%94%EB%B2%BD-%EB%93%B1%EB%B0%98-2412%EB%B2%88-Python

# O(25억)인데 시간초과가 나지 않나..
    # lower_bound + set() 활용
# queue의 pop은, deque.popleft()

# 접근
# 1. (0, 0)에서 조건에 만족하는 홈을 찾아 큐에 넣는다.
# 2. bfs를 돌려가며, 각 홈에서 조건에 만족하는 홈을 찾는다. + (x, y, dis)
# 3. dis 값이 더 작은 것으로 유지한다.
# 4. y좌표가 T일 때 함수를 종료한다.

import sys
from collections import deque
input = sys.stdin.readline

# n : 홈의 개수, T : y좌표가 T가 될 때까지
n, T = map(int, input().split())

# x, y : 홈의 좌표
dot = set()
for _ in range(n):
    x, y = map(int, input().split())
    dot.add((x, y))

q = deque()
q.append((0, 0, 0))

while len(q) > 0:
    curX, curY, curDis = q.popleft() # 그 지점까지 이동한 거리

    if curY == T: # y좌표가 조건 T에 도달하면
        print(curDis) # 이동한 거리를 출력하고 exit()
        exit()

    # lower_bound, 다음 홈으로 갈 수 있는 범위 내만 탐색하면 된다.
    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = curX + i
            ny = curY + j

            if (nx, ny) in dot:
                q.append((nx, ny, curDis + 1))
                dot.remove((nx, ny)) # 삭제하지 않으면, 이제는 더 이상 쓸모없는 홈 좌표가 큐에 계속 맴돌게 됨

print(-1) # 정상에 오를 수 없는 경우