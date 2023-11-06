# 풀이 시간 : 1시간 20분 + 1시간
# 시간복잡도 : O(Nlog(max(lst)))
    # N : isPossible()
    # log(max(lst)) : max(lst)는 최대 10000
# 공간복잡도 : O(N)
# 참고 : https://blogshine.tistory.com/151

# 초기 접근법
    # 구간의 '최댓값' - '최솟값' 이 작아야 함
    # 초기 구간은 '1개'이다.
    # 리스트의 길이를 중심으로 '최댓값 - 최솟값'(x)이 최소가 되게끔 2개의 구간을 만든다.
    # 위 구간들을 중 x가 가장 큰 범위를 다시 구간화한다.
    # 문제점 : 맨 처음 중앙을 분기로 나눴을 때 정확하지 않음


N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 구간 개수 return
# '최대 - 최소'가 mid보다 큰 구간을 count 한다.
def isPossible(mid):
    count = 1
    minV, maxV = lst[0], lst[0]

    for k in lst:
        if k < minV:
            minV = k

        if k > maxV:
            maxV = k

        if (maxV - minV) > mid:
            count += 1
            minV = k
            maxV = k

    return count


def search(start, end):
    result = float('inf')
    while start < end:
        mid = (start + end) // 2 # 구간의 (최댓값 - 최솟값) 의 모음 xList 중 최솟값에 해당하는 값

        # 원하는 구간 개수인 'M'보다 많은 구간이 나왔을 시
            # mid를 크게 설정해, 구간 개수를 좁혀준다.
        if isPossible(mid) > M:
            start = mid + 1

        else:
            result = min(result, mid)
            end = mid

    return result

print(search(0, max(lst)))