import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[][] dp; //공통되는 부분 수열이 길이가 최대 몇까지 되는지 담는 공간
    static String one; //입력받은 첫번째 문자열
    static String two; //입력받은 두번째 문자열
    static char[] char_one; //one을 char[] 배열로 변환, 문자 비교를 위해
    static char[] char_two; //two를 char[] 배열로 변환, 문자 비교를 위해

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        one = br.readLine();
        two = br.readLine();

        char_one = one.toCharArray();
        char_two = two.toCharArray();

        //+1을 함으로써 dp[0][0], dp[i-1][j-1] 공간 탐색할 때 범위 체크를 피해준다. 
        dp = new int[one.length()+1][two.length()+1];

        LCS2(one.length(), two.length());

        //맨 꼭짓점에서는 제일 긴 공통되는 부분 수열(LCS)가 저장된다. 
        System.out.println(dp[one.length()][two.length()]);
    }
    
    //Bottom-up 방식
    private static void LCS2(int one, int two) {
        for(int i=0;i<one;++i){
            for(int j=0;j<two;++j){
                //표로 그려봤을 때, 이와 같은 규칙을 찾을 수 있다.
                if(char_one[i] == char_two[j]){
                    dp[i+1][j+1] = dp[i][j] + 1;
                }
                else
                    dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
            }
        }
    }
}