

# n : n번째 글자
# l : 이전 차수의 길이
# k : 새로운 차수
def solve(n, l, k):
    slen = 2 * l + (k + 3)

    if n <= 3:
        print(moo[n-1])
        return

    # n번째 글자를 구할만큼 moo 문자열의 길이가 충분치 않을 때
    elif slen < n:
        solve(n, slen, k+1)


    # 충분한 moo 문자열의 길이
    else:
        # 중간 구간
        if n <= (l + k + 3):
            if n - l == 1:
                print("m")
            else:
                print("o")
            return

        # 마지막 구간
        # 첫번째∙중간 구간을 빼, 첫번째 구간처럼 볼 수 있게 한다.
        else:
            solve(n-(l + k + 3), 3, 1)


moo = ['m', 'o', 'o']
N = int(input())

solve(N, 3, 1)