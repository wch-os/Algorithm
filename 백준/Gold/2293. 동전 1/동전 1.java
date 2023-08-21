//참고
//https://yabmoons.tistory.com/491

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] coin;
    static int[] dp;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); //동전의 개수
        int K = Integer.parseInt(st.nextToken()); //만들고자 하는 가치

        coin = new int[N];
        dp = new int[K+1]; //해당 가치를 만들 수 있는 경우의 수

        for (int i = 0; i < N; ++i) {
            int coinOne = Integer.parseInt(br.readLine());
            coin[i] = coinOne;
        }

        dp[0] = 1; //어떤 동전도 사용하지 말아야하는 경우의 수

        //K 가치를 구하기 위해서 사용되는 경우의 수
        int result = solve(K);
        System.out.println(result);
    }

    private static int solve(int K) {
        //동전의 종류마다 최대 k번까지 경우의 수가 갱신된다.
        for (int i = 0; i < N; ++i) {
            //동전의 크기를 첫번째 동전 크기부터, k원까지 늘린다.
            for (int j = 1; j <= K; ++j) {
                //가치보다 작은 동전의 경우, 가치 계산
                if (coin[i] <= j) {
                    //이전 dp + dp[j-현재 사용한 동전의 종류 크기] //dp[j-coin[i]]에서 coin[i] 동전을 사용하는 경우의 수
                    dp[j] += dp[j-coin[i]];
                }
            }
        }
        return dp[K];
    }
}