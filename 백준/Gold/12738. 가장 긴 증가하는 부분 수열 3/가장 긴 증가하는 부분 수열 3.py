# 참고 : https://st-lab.tistory.com/285

def solve(start, end, push):
    while start <= end:
        mid = (start + end) // 2

        # 넣을 값보다 큰 값이면
        if result[mid] >= push:
            end = mid - 1

        # 넣을 값보다 작은 값이면,
        elif result[mid] < push:
            start = mid + 1

    # end : mid - 1 함으로써, 넣을 값(push)과 가장 가까운 작은 값의 인덱스가 됨
    # end + 1 : 넣을 값(push)과 가장 가까운 큰 값의 인덱스
    return end+1



N = int(input()) # 수열의 크기
lst = list(map(int, input().split())) # 수열
result = [lst[0]] # 증가하는 부분수열(대체되는 수 가능) 담은 자료구조

for i in range(1, N):
    # 증가하는 수열이면, 그냥 추가
    if lst[i] > result[-1]:
        result.append(lst[i])

    # 감소라 해야하나, 증가하는 수열에서 중간값이 대체될 수 있는 수
    else:
        idx = solve(0, len(result), lst[i])
        result[idx] = lst[i]


# 증가하는 부분수열의 길이 출력
print(len(result))