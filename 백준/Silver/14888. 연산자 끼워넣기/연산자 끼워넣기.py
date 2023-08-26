#참고
#https://st-lab.tistory.com/121
#https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python

N = int(input()) # 수의 개수
number = list(map(int, input().split())) # 주어진 수
operator = list(map(int, input().split())) # 각 연산자의 개수

maxValue = -float('inf')
minValue = float('inf')

# 넘겨받은 수, 다음 수 인덱스
def dfs(num, idx):
    global maxValue, minValue

    # 모든 연산이 끝났을 때, 최댓값∙최솟값 구하기
    if idx == N:
        maxValue = max(maxValue, num)
        minValue = min(minValue, num)

    # 아직 모든 연산이 끝나지 않았으면
    else:

        # 남아있는 연산자 수를 체크한다.
        for i in range(len(operator)):

            # 각 연산자의 숫자가 남아있으면
            if operator[i] > 0:

                # 해당 연산자 수 1개 감소
                operator[i] -= 1

                if i==0: #덧셈
                    dfs(num + number[idx], idx+1)

                elif i==1: #뺄셈
                    dfs(num - number[idx], idx+1)

                elif i==2: #곱셈
                    dfs(num * number[idx], idx+1)

                elif i==3: #나눗셈
                    #파이썬에서는 음수 // 몫을 구할 때 내림값을 return 한다.
                    dfs(int(num / number[idx]), idx+1)

                # 재귀가 끝났으면, 즉 재귀로 인한 모든 연산이 끝났으면
                # 다음 연산을 위해, 다시 해당 연산자 개수를 복구한다.
                operator[i] += 1


dfs(number[0], 1)
print(maxValue)
print(minValue)