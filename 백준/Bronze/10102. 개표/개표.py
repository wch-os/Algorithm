V = int(input())
vote = list(input())

cntA, cntB = 0, 0
for v in vote:
    if v == "A":
        cntA += 1
    else:
        cntB += 1

if cntA > cntB:
    print("A")
elif cntA < cntB:
    print("B")
else:
    print("Tie")