# 풀이 시간 : 35분
# 시간복잡도 : O(NlogN + NlogL)
# 공간복잡도 : O(N)
# 참고 :

# 문제에서 요구하는 값을 범위로 둘 수 있는지 생각해보자.
# 휴게소를 M개 더 지어서 휴게소가 없는 구간의 길이의 최댓값의 최솟값을 찾아야 한다.
# 그러므로 최댓값의 최솟값을 범위로 설정하고 mid 값을 만들기 위해서, 몇 개의 휴게소가 필요한지를 이분탐색 하자

# O(N)
# 체크. mid 값을 만들기 위해서, M개 이하의 휴게소 설치가 필요한가?
def check(minDis):
    setHouse = 0

    for dis in distances:
        if dis > minDis:
            setHouse += ((dis - 1)// minDis) # 휴게소를 설치하여, minDis 이하로 맞추기

    return setHouse <= M

# O(logL)
def bns():
    # check(0): 0 거리를 만들기 위해서는 M개 초과의 휴게소 필요, False
    # check(L): L 거리를 만들기 위해서는 0개로도 가능, True
    lo, hi = 0, L

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if not check(mid):
            lo = mid
        else:
            hi = mid

    return hi



N, M, L = map(int, input().split())
lst = list(map(int, input().split()))
lst.append(0) # 출발점
lst.append(L) # 도착점
lst.sort()

distances = []
for i in range(1, len(lst)):
    distances.append(abs(lst[i] - lst[i-1]))

print(bns())