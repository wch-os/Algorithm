def dfs(depth):
    global result

    if depth == K:
        result = max(result, int("".join(map(str, numbers))))
        return

    for i in range(len(N)-1):
        for j in range(i+1, len(N)):
            # 백트래킹 완전 탐색
            numbers[i], numbers[j] = numbers[j], numbers[i]

            # 이전에 탐색한 노드면 제외한다.
            check = int("".join(map(str, numbers))) * 10 + depth # 튜플이 아닌, 일반 정수 교유값으로 최적화
            if check not in visited:
                dfs(depth+1)
                visited.append(check)

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