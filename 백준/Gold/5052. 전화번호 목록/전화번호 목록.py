# 이전 코드 : 트리에 모든 num을 insert() 하고, 길이가 짧은 번호부터 일관성 체크를 진행한다.
# 현재 코드 : 길이가 짧은 번호부터, 일관성 체크를 하고 insert() 한다.

# 참고 : https://alpyrithm.tistory.com/72
# https://m.blog.naver.com/cjsencks/221740232900
# https://velog.io/@cjkangme/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8A%B8%EB%9D%BC%EC%9D%B4Trie-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self, key, isLeaf=None):
        self.key = key
        self.isLeaf = isLeaf
        self.children = {}

class Trie:
    # Trie 헤드 노드 생성
    def __init__(self):
        self.head = TrieNode(None)

    def insert(self, string):
        # 트리 헤드
        curr_node = self.head

        for s in string:
            # 현재 노드에 해당하는 글자의 자식이 없다면 새로운 노드로 추가
            if s not in curr_node.children:
                curr_node.children[s] = TrieNode(s)

            # 다음 노드로 이동
            curr_node = curr_node.children[s]

        # 리프노드에 '전체 문자열' 저장
        curr_node.isLeaf = string


    def search(self, string):
        curr_node = self.head

        for s in string:
            if s in curr_node.children:
                curr_node = curr_node.children[s]
            else: # 존재하지 않는 s이면 break 이후, 리프노드인지 확인한다.
                break

        # curr_node가 리프노드인 것은 일관성이 없는 번호임을 의미한다.
        # 911, 9112 → NO
        if curr_node.isLeaf:
            return False

        # 남아있지 않으면 일관성 있는 독립적인 번호이다.
        # 911, 912 → YES
        else:
            return True



T = int(input().strip())
for t in range(T):
    N = int(input())
    nums = []
    trie = Trie()
    flag = True

    for _ in range(N):
        num = input().strip()
        nums.append(num)

    # 길이가 짧은 전화번호부터 search를 진행한다.
        # 일관성 체크를 더 빠르게 하기 위함.
    nums.sort()
    for num in nums:
        # 일관성 없는 번호일 경우 break
        if not trie.search(num):
            flag = False
            break

        trie.insert(num)

    if flag:
        print("YES")
    else:
        print("NO")