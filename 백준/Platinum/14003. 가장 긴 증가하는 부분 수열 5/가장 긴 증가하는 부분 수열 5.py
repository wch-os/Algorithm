# 풀이 시간 : 55분 + 30분
# 시간복잡도 : O(N * log(len(LIS))
    # N: 입력 리스트를 차례대로 순회, LIS 데이터인지 판단
    # log(len(LIS)): LIS 이분탐색하여 갱신할 인덱스 구함
# 공간복잡도 : O(N)
# 참고 : -

"""이전 제출코드와의 차이점"""
# 가독성을 위해 기존 result 배열을 알고리즘 유형에 맞게 LIS 로 바꾸었다.
    # LIS(Longest Increasing Subsequence, 최장 증가 수열)

"""기존 LIS 문제와의 차이점"""
# LIS 수열의 갯수를 출력하는 문제는 LIS 배열 내에서 이분탐색을 통해 값을 갱신하면 된다.
# 수열의 데이터를 추가로 출력하는 데 있어서는 추가적인 작업이 필요하다.

"""역추적"""
# 일단 LIS 수열의 끝 값은, 기존 LIS 수열의 이상이 수열이 오지 않는 이상 바뀌지 않는다.
# 따라서 "끝 값"을 기준으로 역추적으로 접근하는 것이 유용해 보인다.
    # 우선 이분탐색을 통해 값을 갱신하는 시점을 (해당 idx, value) 형태로 모두 DP 에 저장한다.
    # 구해진 LIS (길이는 O, 데이터는 불완전) 를 뒤에서부터 차례대로 탐색하여, LIU idx 값에 맞는 value 값을 역추적 시 답을 구할 수 있다.



# lowerBound
def bns(idx):
    lo, hi = -1, len(LIS)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if LIS[mid] < lst[idx]:
            lo = mid

        else:
            hi = mid

    return hi


N = int(input())
lst = list(map(int, input().split()))

LIS = [lst[0]] # 초기값
DP = [(0, lst[0])] # 역추적을 위한 자료구조, (순서, 값)

for i in range(1, len(lst)):
    if LIS[-1] < lst[i]:
        LIS.append(lst[i])
        DP.append((len(LIS)-1, lst[i]))

    else:
        idx = bns(i)
        LIS[idx] = lst[i] # lst[i]에 대한 lowerBound 인덱스(idx)를 찾아, LIS[idx] 위치에 대체함
        DP.append((idx, lst[i]))


# 역추적
result = []
lastIdx = len(LIS) - 1
for i in range(len(DP)-1, -1, -1):
    if DP[i][0] == lastIdx:
        result.append(DP[i][1])
        lastIdx -= 1

print(len(result))
print(*result[::-1])