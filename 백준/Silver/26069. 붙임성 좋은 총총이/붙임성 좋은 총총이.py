N = int(input())

dance = set()
dance.add("ChongChong")

for _ in range(N):
    a, b = map(str, input().split())

    # 옆 사람이 춤추고 있으면
    if a in dance:
        dance.add(b)

    elif b in dance:
        dance.add(a)

print(len(dance))