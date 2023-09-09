import sys
input = sys.stdin.readline

N, M = map(int, input().split())

package = []
one = []
for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    one.append(b)

# 패키지 중 가장 싼 & 1개당 가장 싼 브랜드 찾기
package.sort()
one.sort()

result = 0
# 개별로 사는 것이 더 이득인 경우
if (package[0] // 6) >= one[0]:
    result = one[0] * N

else:
    # 패키지로 먼저 구매한 후
    result += (package[0] * (N//6))

    # over 구매, 개별 구매 중 더 이득인 방법으로
    result += min(N%6 * one[0], package[0])

print(result)