# 풀이 시간 : 1시간 30분 + 1시간
# 시간복잡도 : O(15^10 - 중복탐색)
# 공간복잡도 : O(n)
# 참고 : https://www.youtube.com/watch?v=vGU8h1rneGw

# 입력 3번을 보면 dp로 풀 수 없음.
    # 이전 dp[i-1], dp[i-2]를 활용한 규칙성을 찾을 수 없다.

# 1번째 자릿수를, 제일 큰 수를 찾아바꾸기
# 그리디하게 풀려고 했지만 방법을 찾지 못해 포기

# 풀이
# 기본적으로 dfs로 완전 탐색을 한다는 생각으로 접근을 하고 백트래킹 하여,
# (k : 남은 교환횟수, num : 현재 만들어진 숫자)의 중복된 탐색을 하지 않도록 하여 풀어야 했다.

def check(depth):
    # 이전에 탐색한 노드면 제외한다.
    n = int("".join(map(str, numbers))) * 10 + depth  # 튜플이 아닌, 일반 정수 교유값으로 최적화
    if n in visited:
        return False

    # 처음 가 본 노드라면 계속 탐색을 진행한다.
    visited.append(n)
    return True

def dfs(depth):
    global result

    if depth == K:
        result = max(result, int("".join(map(str, numbers))))
        return

    for i in range(len(N)-1):
        for j in range(i+1, len(N)):
            # 백트래킹 완전 탐색
            numbers[i], numbers[j] = numbers[j], numbers[i]

            if check(depth):
                dfs(depth+1)

            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for t in range(1, T+1):
    N, K = map(str, input().split()) #정해진 숫자, 최대 교환 횟수
    K = int(K)

    numbers = [] #각각의 숫자로 쪼개어 저장하는 자료구조
    visited = [] # 중복 탐색을 하지 않기 위해, (k : 남은 교환횟수, num : 현재 만들어진 숫자) 저장

    result = 0
    for n in N:
        numbers.append(n)

    dfs(0)
    print(f"#{t} {result}")