# 참고 1): https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11401-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-3-%EA%B3%A8%EB%93%9C1-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5
# 참고 2): https://rhdtka21.tistory.com/123

# "모듈러 연산, 페르마의 소정리" 적용
# nCr = n! / (n-r)!r!
# 항상 % p 계산

N, R = map(int, input().split())
p = 1000000007

# 팩토리얼 계산
def factorial(N):
    n = 1
    for i in range(2, N+1): # N까지 포함
        n = (n*i) % p

    return n


# '페르마의 소정리'에서 {(n-r)! r!}^(p-2)}를 위한 함수
def power(N, R):
    if R == 0:
        return 1
    elif R == 1:
        return N

    # '모듈러 연산'을 이용한 연산 횟수 줄이기
    tmp = power(N, R//2)
    if R%2 == 0:
        return tmp * tmp % p
    else:
        return tmp * tmp * N % p

top = factorial(N)
bot = factorial(N-R) * factorial(R) % p



# '페르마의 소정리' 공식 적용
print(top * power(bot, p-2) % p)