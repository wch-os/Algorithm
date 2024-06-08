# 풀이 시간: 25분(초기) + 15분(유형) + 20분
# 시간복잡도: O(N)
# 공간복잡도: O(N)
# 유형: stack
# 참고: https://velog.io/@waoderboy/%EB%B0%B1%EC%A4%80-17298-%EC%98%A4%ED%81%B0%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 브루트포스로는 O(N^2) 시간초과이다.
# 따라서 dp로 접근해서 풀다가, 안풀려서 문제 유형을 보고 방향을 틀었다.
# 스택 문제는 항상 새롭고, 좋다!
    # 오큰수를 못 찾은 수들을 리스트에 저장하고, 추후에 큰 수를 만났을 때 스택 최상단부터 확인하여 업데이트 하는 문제

N = int(input())
lst = list(map(int, input().split()))
indexStack = [0] # 오큰수를 못 찾고 있는 lst 인덱스 리스트

NGE = [-1] * N # 오큰수 기본값 -1
for i in range(1, N):

    # 한 번 큰 수를 만나 오큰수를 찾으면, 이전의 못 찾은 값들도 다시 비교해본다.(이 때 스택 최상단만 비교해보면 된다.)
    while indexStack and lst[indexStack[-1]] < lst[i]:
        NGE[indexStack.pop()] = lst[i]

    indexStack.append(i)

print(*NGE)