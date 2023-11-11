# 풀이 시간 : 2시간 + 1시간
# 시간복잡도 : O(Nlog(K))
# 공간복잡도 : O(1)
# 참고 : https://kbw1101.tistory.com/29

# 이 문제의 핵심은, lst[K]의 정의이다.
    # lst[K] = x 일 때,
    # x보다 작거나 같은 값이 K개 있다는 의미

    # 따라서 범위(1~K) 내에서 mid 값보다 작거나 같은 값이 K개가 되는 최적값을 찾아 반환한다.

N = int(input())
K = int(input())

def search(start, end):
    while start < end:
        mid = (start + end) // 2

        # mid보다 작거나 같은 i*j값 찾기
        cnt = 0
        for i in range(1, N + 1):
            # 각 행의 col 값은 행(i)의 배수이므로,
                # 작은 값을 찾을 때 //i 를 해주면 된다.
            cnt += min(mid // i, N)

        if cnt < K:
            start = mid + 1

        else:
            end = mid

    return end


# end가 'K'인 이유
    # B[k]의 값은 k보다 작거나 같기 때문이다.
    # 1행의 값 때문에 '1~n'은 보장된다.
print(search(1, K))