// 일관성 없는 전화번호 목록이라도, 일단 입력은 끝까지 받아야한다.
// "1234", "123" 처리만 하고 "123", "1234" 일 때의 처리는 하지 않았다.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class TrieNode {
    Map<Character, TrieNode> childNodes = new HashMap<>();
    boolean isLeaf = false;
}

class Trie {
    TrieNode rootNode;

    public Trie() {
        this.rootNode = new TrieNode();
    }

    void insert(String word) {
        TrieNode node = this.rootNode;

        for (int i = 0; i < word.length(); ++i) {
            node = node.childNodes.computeIfAbsent(word.charAt(i), character -> new TrieNode());
        }

        node.isLeaf = true;
    }

    boolean search(String word) {
        TrieNode node = this.rootNode;

        for (int i = 0; i < word.length(); ++i) {
            node = node.childNodes.getOrDefault(word.charAt(i), null);

            // 중간에 값이 없을 때, 일관성이 있는 전화번호 목록일 때이다.
            // ex. "12340", "12341"
            if (node == null) {
                return true; // 일관성이 있다.
            }

            // 중간 노드가 리프노드로 존재할 시
            // ex. "1234", "123" → '3'일 때 걸림
            if (node.isLeaf) {
                return false; // 일관성이 없다.
            }
        }

        // word의 마지막 노드가 이전에 자식노드가 없을 시, 처음 삽입된 것이므로
        // ex. "123"
        if (node.childNodes.isEmpty()) {
            return true;
        }
        // ex. "123", "1234"
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; ++i) {
            Trie trie = new Trie();
            boolean consistencyFlag = true;

            int N = Integer.parseInt(br.readLine());
            for (int j = 0; j < N; ++j) {
                String number = br.readLine();

                // 입력값은 일단 계속 받아야 한다.
                if (consistencyFlag == false) {
                    continue;
                }

                // 삽입하기 전에 Trie 자료구조에서 지금 number가 일관성 있는지 체크한다.
                boolean consistency = trie.search(number);

                // 일관성이 있다면 삽입해준다.
                if (consistency) {
                    trie.insert(number);
                }
                // 일관성이 없다면 이후 전화번호는 볼 필요가 없다.
                else {
                    consistencyFlag = false;
                }
            }

            if (consistencyFlag) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}