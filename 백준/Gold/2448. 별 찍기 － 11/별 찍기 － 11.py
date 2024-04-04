# 풀이 시간 : -
# 시간복잡도 : O(시그마 3*2^n)
# 공간복잡도 : O(n*2n)
# 참고 : -


def funct(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    star = []
    arr = funct(n//2)
    for i in arr:
        star.append(' ' * (n//2) + i + ' ' * (n//2)) # 행에 맞는 양 빈 공간이 필요하다

    for i in arr:
        star.append(i + ' ' + i) # 그 전 재귀에 있는 삼각형을 그대로 왼 / 오 복제한다.

    return star

N = int(input())
print('\n'.join(funct(N))) # \n 으로 star 리스트 구분