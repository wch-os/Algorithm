A, B = map(int, input().split())

aSet = set(map(int, input().split()))
bSet = set(map(int, input().split()))

union = aSet | bSet # 합집합
intersection = aSet & bSet # 교집합

result = union - intersection # 대칭차집합
print(len(result))

