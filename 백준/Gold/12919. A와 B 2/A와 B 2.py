# 풀이 시간 : 15+40분
# 시간복잡도 : O(2^n) - backtrack
# 공간복잡도 : O(n)
# 참고 코드 : https://bio-info.tistory.com/161

# ? : S=1, T=50일 때, 최대 시간복잡도가 O(2^50) 시간초과 나지 않을까? → 역시 시간초과
# Answer : start를 end로 바꾸는 것이 아니라, end를 start로 바꾼다.
# end의 상태에 따라, 2가지 방식을 적용할 수 있다.
# ex. end가 A로만 이루어져 있다면, B를 추가하는 연산을 사용하지 않는다.

# 추가로, A-B를 실제로 제거하고 뒤집는 e를 재귀 돌리는 것이 아니라, 백트래킹이 될 수 있도록 제거를 가정한 e를 재귀해야한다.

def dfs(e):
    # e를 start, 초기 문자로 바꾸었을 때 성공.
    if e == start:
        print(1)
        exit()

    if len(e) == 0:
        return

    if e[-1] == "A":
        # e = e[:-1]
        # dfs(e)
        dfs(e[:-1]) # 마지막 문자 "A"를 지운다.

    if e[0] == "B":
        # e = e[1:]
        # e = e[::-1]
        # dfs(e)
        dfs(e[1:][::-1]) # 첫 문자 "B"를 지우고, 문자열을 뒤집는다.

start = input()
end = input()

dfs(end)
print(0)  # 바꿀 수 없을 때 "0" 출력

# 마지막 문자가 "A"도 아니고 첫 문자가 "B"도 아니면, 만들 수 없는 문자이다.