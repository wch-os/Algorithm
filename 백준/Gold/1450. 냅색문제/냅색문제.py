# 풀이 시간: a + 1시간 20분
# 시간복잡도: O(2^(N/2) * (2^(N/2) *log(2^(N/2)))
    # 2^(N/2): 2개의 부분집합으로 쪼개어, 부분집합 합 리스트를 생성 복잡도
    # (2^(N/2) *log(2^(N/2)): sumA의 모든 원소에 대한 sumB에서의 upperBound 이분탐색 복잡도
# 공간복잡도: O(2^(N/2)
# 유형: MITM, 이분탐색
# 참고: https://ca.ramel.be/100

# MITM(Meet In The Middle)
    # 브루트포스 알고리즘을 사용해야 할 경우, 브루트포스를 분할해서 복잡도를 최소화하는 알고리즘 기법이다.

    # 분할정복과의 차이점?
        # 분할정복은 작은 문제들의 해결을 합치면서, 큰 문제의 해결로 이어져 나간다.
        # MITM 문제를 쪼개는 것은 같지만, 중간에서 만나 결합하는 과정에서 +a의 추가적인 연산이 필요하다.

# 부분집합 합 리스트를 생성한다.
def createPartialSumList(wList, sumList, idx, currentSum):
    if idx == len(wList):
        sumList.append(currentSum)
        return

    createPartialSumList(wList, sumList, idx + 1, currentSum) # 현재 요소를 포함하지 않는 경우
    createPartialSumList(wList, sumList, idx + 1, currentSum + wList[idx]) # 현재 요소를 포함하는 경우


# upperBound를 찾는다. 0 ~ upperBound index 전까지 짐을 넣을 수 있다.
def bns(sumB, k):

    lo, hi = -1, len(sumB)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if sumB[mid] <= k:
            lo = mid
        else:
            hi = mid

    return hi


def main():
    N, C = map(int, input().split())
    weight = list(map(int, input().split()))

    mid = len(weight) // 2
    weightA = weight[:mid]
    weightB = weight[mid:]

    sumA = []
    sumB = []

    createPartialSumList(weightA, sumA, 0, 0)  # 부분집합 합
    createPartialSumList(weightB, sumB, 0, 0)

    # "sumA의 원소 + sumB의 원소 <= C"인 경우의 수를 체크해야 된다.
    # sumA와 sumB 각 원소의 갯수는 최대 2^15
    # 일반적으로 체크할 시 복잡도는, (2^15) * (2^15) 가 된다.
    # 따라서 sumB를 정렬을 진행하고, sumA의 lowerBound를 찾아 하위에 있는 경우의 수는 모두 포함시키도록 하자.
    sumB.sort()

    result = 0
    for k in sumA:
        idx = bns(sumB, C-k) # C-k 무게 이하로 넣어야 한다.
        result += idx

    print(result)


if __name__ == "__main__":
    main()