// 풀이 시간 : 15분 + 10분(생각) + 1시간
// 시간복잡도
    // N : 모든 문자열 갯수, L : 문자열 최대 길이
    // 생성 : O(N * L)
    // 탐색 : O(L)
// 공간복잡도 : O(ML)
// 참고
    // 구현 : https://melody-coding.tistory.com/154
    // 트라이 : https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%9D%BC%EC%9D%B4-Trie
    //         https://codingnojam.tistory.com/40

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

class TrieNode{
    Map<Character, TrieNode> childNodes = new HashMap<>();
    boolean isLeaf = true;
}

class Trie{
    TrieNode rootNode;

    public Trie() {
        this.rootNode = new TrieNode();
    }

    void insert(String word) {
        TrieNode node = this.rootNode;

        // 문자열의 각 단어마다 가져와서 자식노드 중에 있는지 체크
        // 없으면 자식노드 새로 생성
        for (int i = 0; i < word.length(); ++i) {
            node = node.childNodes.computeIfAbsent(word.charAt(i), c -> new TrieNode());

        }

        // 리프노드 임을 명시
        node.isLeaf = true;
    }

    boolean search(String word) {
        TrieNode node = this.rootNode;

        for (int i = 0; i < word.length(); ++i) {
            // 문자열의 각 단어에 매핑된 노드가 존재하면 가져온다.
            node = node.childNodes.getOrDefault(word.charAt(i), null);

            // 없으면, 현재 Trie에 해당 문자열이 없다.
            if (node == null) {
                return false;
            }
        }

        // 현재 노드가 단어의 끝인지 아닌지 체크하는 변수
        return node.isLeaf;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Trie trie = new Trie();
        int count = 0;

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; ++i) {
            trie.insert(br.readLine());
        }

        for (int i = 0; i < M; ++i) {
            boolean bool = trie.search(br.readLine());

            if (bool) {
                count += 1;
            }
        }

        System.out.println(count);
    }
}