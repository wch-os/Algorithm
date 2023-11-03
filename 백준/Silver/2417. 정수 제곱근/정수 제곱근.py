# 풀이 시간 : 10분
# 시간복잡도 : O(logn)
# 공간복잡도 : -
# 참고 : 개념 정리
    # 등호 판단 : 1) https://blossoming-man.tistory.com/entry/%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-Binary-Search-%EA%B2%BD%EA%B3%84-%EC%84%A4%EC%A0%95%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%95%B4%EC%95%BC-%ED%95%98%EB%8A%94%EA%B0%80
    #           2) https://eine.tistory.com/entry/%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89binary-search-%EA%B5%AC%ED%98%84%EC%8B%9C-%EA%B3%A0%EB%A0%A4%ED%95%A0-%EA%B2%83%EB%93%A4
    # Lower, Upper : https://yoongrammer.tistory.com/105

def search(start, end):
    while start < end:
        mid = (start + end) // 2

        if mid * mid < n:
            start = mid + 1

        else:
            end = mid

    return end


n = int(input())

s = 0
e = n

print(search(s, e))