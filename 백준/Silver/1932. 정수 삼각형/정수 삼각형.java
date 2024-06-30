import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] ary; //n개의 수열을 입력받을 공간
    static Integer[][] dp; //범위가 0부터 시작하므로, 빈 공간을 체크하기 위해 Integer 배열을 사용해야 한다.

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine()); //삼각형의 크기를 입력받는다.
        ary = new int[N][N]; //정수 삼각형을 저장하기 위한 배열을 생성한다.
        dp = new Integer[N][N]; //dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-1]) 를 위한 공간을 생성한다.

        for(int i=0;i<N;++i){
            StringTokenizer st = new StringTokenizer(br.readLine());

            int j = 0;
            while(st.hasMoreTokens()){
                ary[i][j] = Integer.parseInt(st.nextToken()); //각 입력을 2차원 배열에 넣는다.
                ++j;
            }
        }

        for(int i=0;i<ary.length;++i){ //N-1, 제일 아래 행은 그대로 복사한다.
            dp[N-1][i] = ary[N-1][i];
        }

        System.out.println(solve2(0,0));//(0,0) 값을 최대값으로 만든다. //합이 최대가 되는 경로에 있는 수의 합을 출력한다.
    }

    private static int solve2(int row, int column){
        if(row == ary.length-1)  //마지막(N-1) 행일 경우 dp 값 리턴 반환
            return dp[row][column];

        if(dp[row][column]==null){ //바로 아래행과 아래행의 오른쪽 열과 비교해서 큰 값을 더한다.
            dp[row][column] = Math.max(solve2(row+1,column),solve2(row+1,column+1))+ary[row][column];
        }
        
        return dp[row][column]; //경로 상의 최대값으로 만든 dp[0][0]을 리턴한다.
    }
}