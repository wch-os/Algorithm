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
            else:
                return False

        # children이 남아있으면 전화번호가 겹치는 것을 의미한다.
        # 911, 9112 → NO
        if curr_node.children:
            return False

        # 남아있지 않으면 일관성 있는 독립적인 번호이다.
        # 911, 912 → YES
        else:
            return True



T = int(input().strip())
for _ in range(T):
    N = int(input())
    nums = []
    trie = Trie()
    flag = True

    for _ in range(N):
        num = input().strip()
        nums.append(num)
        trie.insert(num)

    # 길이가 짧은 전화번호부터 search를 진행한다.
        # 일관성 체크를 더 빠르게 하기 위함.
    nums.sort()
    for num in nums:
        if not trie.search(num):
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")