# *이전 코드가 왜 틀렸는지는 모르겠음
# 그리고 'Slicing Window'를 사용해서 풀어보자

N, K = map(int, input().split())
lst = list(map(int, input().split()))

partSum = sum(lst[:K]) # K번째 직전까지 | K구간 합

_max = partSum # K가 1일 때?
for i in range(N-K):
    # Slicing Window
    partSum += lst[i+K] # 다음 인덱스 더하자
    partSum -= lst[i] # 이전 인덱스 빼자

    _max = max(_max, partSum)

print(_max)