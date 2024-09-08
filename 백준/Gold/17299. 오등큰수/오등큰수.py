# 풀이 시간: 40분(초기) + 15분(참고)
# 시간복잡도: O(N)
# 공간복잡도: O(N)
# 유형: stack
# 참고: https://www.acmicpc.net/source/79380699

# NGF(i) = i보다 횟수가 가장 많이 나오는 숫자
# numsCount(i): i가 등장하는 횟수

# 입력 예제
# nums
# 1 1 2 3 4 2 1
# numsCount
# 3 3 2 1 1 2 3
# NGF
# -1 -1 1 2 2 1 -1

from collections import Counter

N = int(input())
nums = list(map(int, input().split()))
numsCount = Counter(nums)

NGF = [-1] * N # 오등큰수를 끝까지 못 찾는 수의 경우(가장 많이 등장한 숫자), -1의 값을 가진다.
indexStack = [0] # 오등큰수를 못 찾고 있는 nums 인덱스 리스트

for i in range(1, N):

    while indexStack and numsCount[nums[indexStack[-1]]] < numsCount[nums[i]]:
        # nums[i]가 스택에 있는 수보다 더 많이 등장했을 때
        NGF[indexStack.pop()] = nums[i]

    # 오등큰수를 못 찾은 수는 추후에 업데이트 한다.
    indexStack.append(i)

print(*NGF)