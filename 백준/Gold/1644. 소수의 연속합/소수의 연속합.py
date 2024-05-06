# 풀이 시간 : 15분 + 17분
# 시간복잡도 : O(n*log(logn))
# 공간복잡도 : O(n)
# 참고 : -

# 이전 소수 판별은 O(n*sqrt(n))
# '에라토스테네스 채'로 소수 구하기는 O(n*log(logn))

# O(sqrt(N))
def eratos(k):
    for i in range(k*2, N+1, k):
        prime[i] = False


# O(N)
def twoPointer():
    s, e = 0, 0

    sumK = 0
    cnt = 0
    while True:
        if sumK == N: # 소수 연속합으로 N이 만들어지면 cnt++
            cnt += 1

        if sumK > N: # sumK가 더 크면, s 조정
            sumK -= lst[s]
            s += 1

        elif e == len(lst): # e += 1로 len(lst)가 되었음에도, sumK가 작아 e 인덱스 조정으로 index out이 발생할 때
            break

        elif sumK <= N: # sumK == N이어도 다음 경우의 수를 찾아야 하므로, 인덱스 조절이 필요하다
            sumK += lst[e]
            e += 1

    return cnt



N = int(input())

# N 이하의 소수 구하기
lst = []
prime = [False, False] + [True] * (N-1)
for i in range(2, N+1):
    if prime[i]:
        lst.append(i)
        eratos(i)

print(twoPointer())