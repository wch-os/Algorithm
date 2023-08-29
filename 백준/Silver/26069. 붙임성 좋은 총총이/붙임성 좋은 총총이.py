N = int(input())

dance = set()

for _ in range(N):
    a, b = map(str, input().split())

    # 총총을 만나면 dance set에 추가
    if a == "ChongChong" or b == "ChongChong":
        dance.add(a)
        dance.add(b)

    if len(dance) > 0:
        # 옆 사람이 춤추고 있으면
        if a in dance:
            dance.add(b)

        elif b in dance:
            dance.add(a)

print(len(dance))