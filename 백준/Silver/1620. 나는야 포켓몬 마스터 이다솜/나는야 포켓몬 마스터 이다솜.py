import sys
input = sys.stdin.readline

N, M = map(int, input().split())

_dict = dict()
for i in range(1, N+1):
    s = input().rstrip()
    # key가 번호, value가 포켓몬 이름
    # 번호를 search의 문자형과 매칭하기 위해 문자열로 바꿈
    _dict[str(i)] = s
    _dict[s] = str(i)


for i in range(M):
    search = input().rstrip()
    print(_dict[search])