#참고
#https://jiwon-coding.tistory.com/21

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())

lst = []
result = []

def dfs():
    if len(lst) == M: #길이가 M이 되면 출력
        """
          중복되는 수열을 제거하기 위해, 길이가 M인 수열을 모두 정렬시키고 append한다.
        """
        lst.sort()
        if lst not in result:
            result.append(list(lst)) #lst가 변경되도(remove) 영향 x
        return

    for i in range(1, N+1):
        if i not in lst: #중복되지 않은 수 넣기
            lst.append(i)
            dfs() #dfs 탐색하며 길이 M인 수열 찾기, M이 되지 않으면 깊이 탐색

            """
              위에서 list 정렬을 하므로 pop()을 하면 정렬된 원소의 끝 값이 pop() 된다.
            """
            lst.remove(i)

dfs()

for lst in result:
    print(' '.join(map(str, lst)))