import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] ary;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;


        int N = Integer.parseInt(br.readLine());
        ary = new int[N][N];

        for(int i=0;i<N;++i){
            String[] split = br.readLine().split("");
            for(int j=0;j<N;++j){
                ary[i][j] = Integer.parseInt(split[j]);
            }
        }

        divide(N, 0, 0);

        System.out.println(sb);
    }

    public static void divide(int N, int r, int c){
        if(check(N, r, c)) { //압축 가능할 때
            sb.append(ary[r][c]);
        }

        else {
            //쿼드 분할할 때 괄호를 생성해야 함. => 각 공간 분리
            //그리고, 분할이 필요없는 경우 바로 숫자 추가
            sb.append("(");
            for (int i = r; i < r + N; i += N / 2) {
                for (int j = c; j < c + N; j += N / 2) {
                    divide(N/2, i, j);
                }
            }
            sb.append(")");
        }
    }

    //압축 여부 check하는 함수
    private static boolean check(int N, int r, int c) {
        int fix = ary[r][c]; //우상단을 기준으로 정한다.

        for (int i = r; i < r + N; ++i) {
            for (int j = c; j < c + N; ++j) {
                if(fix != ary[i][j]) //압축 불가
                    return false;
            }
        }
        return true;
    }
}