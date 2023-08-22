import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int W[]; //물건의 무게를 담는 배열
    static int V[]; //물건의 가치를 담는 배열

    //각 인덱스가 각 물건마다 가질 수 있는 최대 가치를 담는 배열
    static int dp[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); //물품의 수
        int K = Integer.parseInt(st.nextToken()); //최대로 담을 수 있는 무게

        W = new int[N+1];
        V = new int[N+1];

        //이전 물건에 대한 가치를 메모제이션 할 때, 0번째 물건 가치를 저장하기 위해 N+1 공간
        //무게 K 일 때 최대 가치를 알아내기 위한 K+1 공간을 생성한다.
        dp = new int[K+1];

        //0번째 물건 가치를 비워두기 위해(0) 1부터 시작한다.
        for(int i=1;i<=N;++i){
            st = new StringTokenizer(br.readLine());

            W[i] = Integer.parseInt(st.nextToken()); //물건 무게
            V[i] = Integer.parseInt(st.nextToken()); //물건 가치
        }

        solve3(N, K);
        System.out.println(dp[K]);
    }

    private static void solve3(int N, int K){
        for(int i=1;i<=N;++i){ //N번째 물건

            //무계의 한계치까지 반복 수행한다.
            //각 무게에서 가질 수 있는 최대 가치
            for(int j=K;j-W[i]>=0;--j){
                //N번째 무게의 가치 + 남은 무게의 가치가 크다면 그 값을 갱신해준다.
                dp[j] = Math.max(dp[j], dp[j-W[i]] + V[i]);
            }
        }
    }
}