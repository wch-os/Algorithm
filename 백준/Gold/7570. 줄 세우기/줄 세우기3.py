# 이전 코드 통과하지 못한 반례 : 1,2,4,5,3

N = int(input())
children = list(map(int, input().split()))

idx = [0] * (N+1)
for i, v in enumerate(children):
    idx[v] = i # 값에, children 위치 저장

count = 1
cqMax = 1
for i in range(1, N):
    # 오름차순으로 연속될 숫자일 시, '연속됨'을 카운트
    if idx[i] < idx[i+1]:
        count += 1
        cqMax = max(cqMax, count)
    else:
        count = 1


# 숫자가 1개이면 옮길 필요 없음
if N==1:
    print(0)

# 연속된 숫자를 제외한 N-cqMax 번 재배열하면 된다.
else:
    print(N-cqMax)
