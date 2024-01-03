// 풀이 시간 : 17분
// 시간복잡도 : O(string.length())
// 공간복잡도 : O(string.length())
// 참고 : -

// 생각
    // 1이 맨처음 나왔을 때 시작
    // 0과 1의 연속됨을 체크한다.

// 체크
    // 1) string.charAt()
    // 2) string.toCharArray()


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int i = 1; i <= T; ++i) {
            String memory = br.readLine();
            int result = funct(memory);
            sb.append("#").append(i).append(" ").append(result).append('\n');
        }
        System.out.println(sb);
    }

    private static int funct(String memory) {
        char[] charMemory = memory.toCharArray();
        int count = 0;
        if (charMemory[0] == '1') {
            count++;
        }
        for (int i = 1; i < charMemory.length; ++i) {
            if (charMemory[i - 1] != charMemory[i]) {
                count++;
            }
        }

        return count;
    }
}