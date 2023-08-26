# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())

#
lst = []
def dfs(start):
    #길이가 M이면 출력
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return;

    #같은 수를 여러 번 골라도 된다.
    #중복되는 수열은 안 된다. (1, 2) (2, 1)
    for i in range(start, N+1):
        lst.append(i)
        dfs(i)
        lst.pop()

dfs(1)