# 풀이 시간 : 5분
# 시간복잡도 : O(n)
# 공간복잡도 : O(n)
# 참고 : -

# '0! = 1'만 주의하면 될 듯
# nCm = n! / (n-m)!m!
n, m = map(int, input().split())
fact = [[] for _ in range(n+1)]

fact[0] = 1
fact[1] = 1
for i in range(2, n+1):
    fact[i] = fact[i-1] * i

print(fact[n] // (fact[n-m] * fact[m]))