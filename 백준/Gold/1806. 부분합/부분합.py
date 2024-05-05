# 풀이 시간 : 30분
# 시간복잡도 : O(n)
# 공간복잡도 : O(n)
# 참고 : -

# sum(lst[s:e+1]) 계속 sum을 해주는 과정에서 O(N) 복잡도로 시간초과가 나는 듯 하다.
# 문제에서 주어진 배열을 사용해야 한다.

def twoPointer():
    s, e = 0, 0

    cnt = float('inf')
    sumK = lst[s]
    while True:
        if sumK >= K: # 구간합이 크면
            cnt = min(cnt, e - s + 1)
            sumK -= lst[s]
            s += 1

        else: # 구간합이 작으면
            e += 1

            if e == N:
                break
            else:
                sumK += lst[e]

    if cnt == float('inf'):
        return 0
    else:
        return cnt



N, K = map(int, input().split())
lst = list(map(int, input().split()))

print(twoPointer())