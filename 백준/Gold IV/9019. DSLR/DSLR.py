# 풀이 시간 : 55분 + 15분
# 시간복잡도 : O(bfs)
# 공간복잡도 : O(bfs)
# 참고 : -

# 1. visited 방문 처리를 함으로써 중복 계산 방지
# 2. % 10000
# 3. 리스트 접근 시간에 의한건가.. 그래도 O(1)인데
# 4. 회전할 때 세자릿수일 때를 따로 고려하지 않아도 된다.

from collections import deque

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    visited = [False for _ in range(10000)]
    visited[A] = True

    q = deque()
    q.append([A, ""])

    while q:
        num, command = q.popleft()

        if num == B:
            print(command)
            break

        numD = (num * 2) % 10000
        if not visited[numD]:
            visited[numD] = True
            q.append([numD, command + "D"])
        
        numS = (num - 1) % 10000
        if not visited[numS]:
            visited[numS] = True
            q.append([numS, command + "S"])

        l = len(str(num))
        numL = (num % 1000 * 10) + (num // 1000)
        if not visited[numL]:
            visited[numL] = True
            q.append([numL, command + "L"])

        numR = (num % 10 * 1000) + (num // 10)
        if not visited[numR]:
            visited[numR] = True
            q.append([numR, command + "R"])
