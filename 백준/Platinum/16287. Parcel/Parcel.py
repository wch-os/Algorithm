# 풀이 시간: 30분 + 15분
# 시간복잡도: O(N^2)
    # nC4 → 2 * nC2
# 공간복잡도: O(N^2)
# 유형: mitm, dp
# 참고: https://hellominchan.tistory.com/250

# 처음에 2개의 집합으로 나누고 0~4개 조합을 생각했으나, 시간복잡도 계산에서 시간 초과

# 30분 정도를 로직과 시간복잡도를 계산하다가 블로그를 참고했다.
# 이 문제는 i를 기준으로 2개의 집합으로 나눈다.
# 왼쪽 집합에서는 bottom-up으로 "2개의 부분 원소들의 합"을 구해 방문 표식을 남긴다.
# 오른쪽 집합에서는 대응되는 "W - 2개의 부분 원소들의 합"에 대한 방문 표식이 있는지 확인한다.

# 4개 원소합의 리스트를 구하는 것이 아니라, 4개 원소합이 W인 원소만 구하면 된다.
# 따라서 nC4가 아니라, nC2 + nC2 경우의 수만을 고려하면 된다.

W, N = map(int, input().split())
lst = list(map(int, input().split()))

memoization = [False] * W

for i in range(1, N):

    # i+1을 기준으로, 오른쪽에서 크기가 2인 부분집합을 고른다.
    # 여기에서 i+1은 왼쪽 기준 i가 끝나고 반복문이 1번 끝남으로써 i++이 적용된 i이므로, i+1이라고 명시했다.
    for j in range(i+1, N):
        if lst[i] + lst[j] < W and memoization[W - (lst[i] + lst[j])]:
            print("YES")
            exit()

    # i를 기준으로, 왼쪽에서 크기가 2인 부분집합을 고른다.
    for j in range(i):
        if lst[i] + lst[j] < W:
            memoization[lst[i] + lst[j]] = True

print("NO")