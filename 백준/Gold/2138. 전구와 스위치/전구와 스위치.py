# 풀이 시간 : 50분 + 30분
# 시간복잡도 : O(N)
# 공간복잡도 : O(N)
# 참고 : https://velog.io/@waoderboy/BOJ-%EB%B0%B1%EC%A4%80-2138-%EC%A0%84%EA%B5%AC%EC%99%80-%EC%8A%A4%EC%9C%84%EC%B9%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 지난 코드
    # i 전구 상태 값에 따라 스위치 OX를 결정했다.
    # 문자열을 그대로 입력받아, 문자열 상태를 바꾸도록 했다. → O(N)
        # S = S[:nx] + "0" + S[nx+1:]

# 순차적으로 탐색한다면, i번째 스위치가 i-1번째 전구의 상태를 결정할 마지막 스위치이다.


def change(A, B):
    Acopy = A[:]
    cnt = 0
    for i in range(1, N):
        # i-1 전구 상태 값에 따라 스위치 OX가 결정된다.
        if Acopy[i-1] == B[i-1]:
            continue

        cnt += 1
        for j in range(i-1, i+2):
            if j < N:
                Acopy[j] = 1 - Acopy[j] # Good

    if Acopy == B: # 목표하는 전구 상태가 됐을 시
        return cnt
    else:
        return -1



N = int(input())
S = list(map(int, input()))
E = list(map(int, input()))

# 0번째 스위치 X
res = change(S, E)
if res != -1:
    print(res)

# 0번째 스위치 O
else:
    S[0] = 1 - S[0]
    S[1] = 1 - S[1]

    res = change(S, E)
    if res != -1:
        print(res+1)
    else:
        print(-1)