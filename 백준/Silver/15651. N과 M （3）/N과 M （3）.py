#참고
#https://jiwon-coding.tistory.com/22

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())

lst = []

def dfs():
    if len(lst) == M: #길이가 M이 되면 출력
        print(' '.join(map(str, lst)))
        return

    for i in range(1, N+1):
        """    if i not in lst: #중복되지 않은 수 넣기    """
        lst.append(i)
        dfs()  # dfs 탐색하며 길이 M인 수열 찾기, M이 되지 않으면 깊이 탐색
        lst.pop()

dfs()