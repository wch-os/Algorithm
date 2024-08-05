# 풀이 시간: 35분
# 시간복잡도: O(N+M)
# 공간복잡도: O(N)
# 유형: 문자열, 재귀
# 참고: -

# ABAB가 있을 경우, 첫 번째 A를 먼저 찾아야한다.

# start ~ end 구간에서, 사전순이 높은 문자 찾기 (알파벳이 작은 문자)
def findSmallWords(start, end):
    small = 'z'
    smallIdx = start
    for i in range(start, end+1):
        if small > word[i]:
            small = word[i]
            smallIdx = i

    # word 순서에 맞춰 차례대로 출력해야 함.
    visited[smallIdx] = True
    for i in range(len(word)):
        if visited[i]:
            print(word[i], end = "")
    print()

    return smallIdx

# start ~ end 구간에서, 사전 순으로 가장 앞에 오도록 하는 문자 보여주기
def solve(start, end):
    if start > end:
        return

    # start == end 일 때도 실행
    findIdx = findSmallWords(start, end)

    solve(findIdx + 1, end)
    solve(start, findIdx - 1)



word = input()

result = []
visited = [False for _ in range(len(word))]

solve(0, len(word)-1)