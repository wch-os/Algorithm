# 풀이 시간: 1시간 10분
# 시간복잡도: O(len(S) * a)
# 공간복잡도: O(1)
# 유형: math?
# 참고: -

# prev 인덱스 조절에서 시간을 많이 잡아먹었다..
# 현재중복위치 - 이전중복위치에 대한 길이 계산과 초기화가 까다로움
# leetcode 클래스 형식 맞추기 힘들다;

# Longest Substring Without Repeating Characters (반복되는 문자가 없는 가장 긴 부분 문자열)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        alphaLoc = [-1 for _ in range(128)]  # 알파벳 최신 위치 추적

        # 이전 중복 위치, 조건을 만족하는 길이, 문장 위치
        result, prev, cnt, idx = 0, -1, 0, 0

        for char in s:
            word = ord(char) # 현재 문자의 ASCII 값
            curr = alphaLoc[word] # 알파벳이 방문 여부 (이전 위치를 담고 있음)

            # 첫 방문
            if curr == -1:
                cnt += 1
                alphaLoc[word] = idx

            # 중복 방문
            else:
                result = max(result, cnt)
                cnt -= (curr - prev) # 중복 알파벳 전의 알파벳 개수 (=현재 중복 위치 - 이전 중복 위치)
                cnt += 1  # 현재 알파벳에 대한 count 업데이트

                # 이전 중복위치 +1 ~ 현재 중복위치, 최신 위치 초기화
                for i in range(prev + 1, curr):
                    alphaLoc[ord(s[i])] = -1

                alphaLoc[word] = idx # 중복 방문한 알파벳은 현재 위치로 등록
                prev = curr

            idx += 1

        result = max(result, cnt)
        return result