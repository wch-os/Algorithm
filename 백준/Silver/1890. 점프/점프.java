//경로의 개수는 2^63-1보다 작거나 같다.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N; //게임판의 크기
    static int[][] matrix; //입력값 저장
    static long[][] result; //해당 위치까지 갈 수 있는 경로의 개수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        matrix = new int[N][N];
        result = new long[N][N];

        //게임판 초기화
        for (int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine());
            int j = 0;
            while(st.hasMoreTokens()){
                matrix[i][j] = Integer.valueOf(st.nextToken());
                j++;
            }
        }

        result[0][0] = 1;
        solve();

        System.out.println(result[N - 1][N - 1]);
    }

    private static void solve() {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                //현재 위치에서 이동할 거리 체크
                int K = matrix[i][j];

                if(result[i][j]!=0) {
                    //엔드 지점일 경우 제외
                    if (i == N - 1 && j == N - 1)
                        continue;

                    //이동 위치로 갈 수 있는 경로 개수 체크
                    if (i + K < N)
                        result[i + K][j] += result[i][j];

                    if (j + K < N)
                        result[i][j + K] += result[i][j];
                }
            }
        }
    }
}