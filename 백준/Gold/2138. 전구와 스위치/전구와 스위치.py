# 풀이 시간 : 20분 + 10분
# 시간복잡도 : O(N)
# 공간복잡도 : O(N)
# 유형 : greedy
# 참고 : https://velog.io/@waoderboy/BOJ-%EB%B0%B1%EC%A4%80-2138-%EC%A0%84%EA%B5%AC%EC%99%80-%EC%8A%A4%EC%9C%84%EC%B9%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC

def solve(S, E):
    Scopy = S[:]
    cnt = 0

    for i in range(1, N):
        # i-1번째, 첫번째 전구 상태 값에 따라 스위치 누름 여부가 결정된다.
        if Scopy[i-1] == E[i-1]:
            continue


        cnt += 1
        for j in [i-1, i, i+1]:
            if j < N:
                Scopy[j] = 1 - Scopy[j]

    if Scopy == E: # S와 E의 전구 상태가 같을 시
        return cnt
    else:
        return -1


N = int(input()) # 전구 개수
start = list(map(int, input())) # 초기 상태
end = list(map(int, input())) # 목표 상태

# 0번째 스위치를 누르지 않았을 때
result = solve(start, end)
if result != -1:
    print(result)

# 0번째 스위치를 눌렀을 때
else:
    start[0] = 1 - start[0]
    start[1] = 1 - start[1]
    
    result = solve(start, end)
    
    if result != -1:
        print(result + 1)
    else:
        print(-1)
    