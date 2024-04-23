h, m, s = map(int, input().split())
time = int(input())

s += time
plusM = s // 60
s %= 60

m += plusM
plusH = m // 60
m %= 60

h += plusH
h %= 24

print(f"{h} {m} {s}")