# 참조 : https://growth-coder.tistory.com/127
# 'end' 출력이 아닌 'result' 출력이면
# exit 조건에서 result 갱신을 위해서 start == end 구간을 제외해야 한다. 

import sys
input = sys.stdin.readline

# 이분탐색
def solve(start, end):
    global result

    count = 0
    mid = (start + end) // 2

    if start > end: # 최소 길이, 최대 길이 구간이 역전되면 exit
        print(result)
        exit()

    for item in lst:
        count += item // mid

    if count >= N: # 랜선이 필요한 것 이상으로 나오면, 길이 크게 설정
        result = mid
        solve(mid+1, end)

    elif count < N: # 적게 나오면, 길이 작게 설정
        solve(start, mid-1)

# 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

result = 0
solve(1, max(lst))