result = []

def solve():
    s = 0
    e = N - 1

    while s<=e:
        mid = int((s + e) / 2)

        if numList[mid] == item:
            return True
        elif numList[mid] < item: #찾고자 하는 값이, mid 기준으로 오른쪽에 있는 경우
            s = mid + 1
        else: #mid 기준으로 왼쪽에 있는 경우
            e = mid - 1

    return False

#정수 개수
N = int(input())
#원본 리스트
numList = list(map(int, input().split()))
#이분탐색을 위한 오름차순 정렬
numList.sort();

#정수 개수
M = int(input())
#비교할 리스트
comList = list(map(int, input().split()))

for item in comList:
    if solve():
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)