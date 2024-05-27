# 풀이 시간 : 20분 + 10분
# 시간복잡도 : O(N^2)
# 공간복잡도 : O(N)
# 참고 : https://hbj0209.tistory.com/151

# 두 눈사람의 차이, "snowmanA가 항상 크다." 라는 보장은 없으므로 절댓값 주의
# 정렬을 깜빡했다.. ㅎㅎ

N = int(input())
snow = list(map(int, input().split()))
snow.sort()

diff = float('inf')
for i in range(N-3):
    for j in range(i+3, N):
        snowmanA = snow[i] + snow[j]

        x, y = i + 1, j - 1 # 투포인터
        while x < y: # 같아지면 stop
            snowmanB = snow[x] + snow[y]

            diff = min(diff, abs(snowmanA - snowmanB))
            if diff == 0:
                print(0)
                exit()
            elif snowmanA > snowmanB:
                x += 1
            else:
                y -= 1

print(diff)