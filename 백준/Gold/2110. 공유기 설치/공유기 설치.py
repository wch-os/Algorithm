# 참고 : https://katfun.tistory.com/entry/%EB%B0%B1%EC%A4%80-2110%EB%B2%88-%EA%B3%B5%EC%9C%A0%EA%B8%B0-%EC%84%A4%EC%B9%98
import sys
input = sys.stdin.readline

def solve(start, end):
    global result

    while start <= end:
        mid = (start + end) // 2 # 공유기를 설치할 간격
        current = lst[0]
        count = 1

        # mid 간격으로, 공유기 설치
        for i in range(1, len(lst)):
            # 집의 위치 - 현재 집의 위치 (연속된 집 간격) >= 간격 | 내에 있으면
            if lst[i] - current >= mid:
                count += 1
                current = lst[i]

        # 공유기가 많이 설치되면 , 더 긴 간격으로 설치하기
        if count >= M:
            start = mid + 1
            result = mid

        # 공유기가 적게 설치되면, 더 적은 간격으로 설치하기
        else:
            end = mid - 1



N, M = map(int, input().split()) # 집 개수, 공유기 개수
lst = [int(input()) for _ in range(N)] # 공유기 사이의 거리
lst.sort()  # 차례대로 설치하기 위해 오름차순 정렬

result = 0
solve(1, lst[-1])
print(result)