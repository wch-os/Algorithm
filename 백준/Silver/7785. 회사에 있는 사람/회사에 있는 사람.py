N = int(input()) #출입 기록의 수

company = {}
for _ in range(N):
    a, b = map(str, input().split())

    if b == "enter": #등록
        company[a] = 1

    else: #삭제
        company.pop(a)

# 현재 회사에 있는 사람의 이름을, 사전 순의 역순으로 출력
sorted_company = dict(sorted(company.items(), reverse=True))
for person in sorted_company:
    print(person)