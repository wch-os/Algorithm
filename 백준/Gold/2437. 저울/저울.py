N = int(input())
lst = list(map(int, input().split()))

# 측정 가능한 무게를 최소화하기 위해, 오름차순 정렬
lst.sort()


min_weight = 1 # 측정 가능한 양의 정수 무게

# 'x'를 측정할 수 있다면 'min_weight + x' 도 측정 가능한 양의 정수 무게이다.
# → 'min_weight'에서 'x'를 추가로 올리면 측정이 가능하다.
for x in lst:
    # 만들 수 없는 무게를 찾는 경우
    if min_weight < x:
        break
    min_weight += x

print(min_weight)