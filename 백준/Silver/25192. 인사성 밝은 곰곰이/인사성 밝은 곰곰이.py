N = int(input()) # 채팅방의 기록 수

setList = set()
count = 0
for _ in range(N):
    # 채팅방 문자열
    s = input()

    # Enter 입력
    if s == "ENTER":
        count += len(setList)
        setList.clear()

    # setList 없다면 추가, 이모티콘 카운트
    else:
        setList.add(s)

# 마지막 Set 길이
count += len(setList)

# 이모티콘 사용된 횟수 출력
print(count)