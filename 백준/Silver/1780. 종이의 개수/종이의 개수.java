import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] ary;
    static int minus_count = 0;
    static int zero_count = 0;
    static int plus_count = 0;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        ary = new int[N][N];

        //input
        for(int i=0;i<N;++i){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;++j){
                ary[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        /*
        종이의 크기, 자르고자 하는 부분의 x-y 좌표를 함수의 인자로 전달한다.
         */
        divide(N, 0, 0);

        System.out.println(minus_count);
        System.out.println(zero_count);
        System.out.println(plus_count);
    }

    private static void divide(int N, int a, int b) {
        boolean divide_boolean; //divide 판단 유무를 위한 변수이다.

        //해당 종이의 공간이 모두 같은 수인지 판단하는 함수이다.
        divide_boolean = space_check(N, a, b);


        //divide 경우
        if(divide_boolean) {
            for (int i = a; i < a + N; i += N/3) { //divide의 범위는 "N/3" 이다.
                for (int j = b; j < b + N; j += N/3) {
                    divide(N / 3, i, j); //자른 공간의 "우상단 i, j 좌표"를 넘겨준다.
                }
            }
        }

        //divide 하지 않는 경우
        //즉, 종이가 모두 같은 수일 경우
        else{
            int fix = ary[a][b];

            if(fix>0)
                plus_count++;
            else if(fix<0)
                minus_count++;
            else
                zero_count++;
        }
    }

    private static boolean space_check(int N, int a, int b) {
        int fix = ary[a][b]; //종이가 모두 같은 수인지 판단하기 위한 "우상단 좌표"를 기준으로 정한다.
        for (int i = a; i < a + N; ++i) {
            for (int j = b; j < b + N; ++j) {
                if (fix != ary[i][j]) {
                    return true; //모두 같은 수 아님 -> divide 필요
                }
            }
        }
        return false;
    }
}