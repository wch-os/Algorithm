import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N; // 노드의 수
    static int[][] graph; // 그래프
    static int[][] dp; // 동적 프로그래밍을 위한 배열
    static final int INF = 987654321; // 무한대

    static int dfs(int now, int visited) {
        // 모든 노드를 방문했을 시
        if (visited == (1 << N) - 1) {
            if (graph[now][0] != 0) // 시작점까지 가는 경로
                return graph[now][0];
            return INF; // 없으면 INF 값 반환
        }

        // 중복 경로일 시 이전 구한 값 return
        if (dp[now][visited] != 0)
            return dp[now][visited];

        // 노드 방문
        dp[now][visited] = INF; // 방문 표시, 길이 없어도 "if dp[now][visited] != 0"이 무한 재귀가 되지 않도록
        for (int i = 0; i < N; i++) {
            if (graph[now][i] == 0)
                continue;

            // i가 이전에 방문한 노드인지 판단 ("&")
            if ((visited & (1 << i)) != 0)
                continue;

            // i 노드를 방문한다. ("|")
            // 그리고, 방문하지 않은 노드들을 방문했을 때 걸리는 최소 비용을 temp에 저장한다.
            int temp = dfs(i, visited | (1 << i));

            // 현재 노드에서 i까지 비용 + temp 와 비교한다.
            dp[now][visited] = Math.min(dp[now][visited], graph[now][i] + temp);
        }

        return dp[now][visited];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        graph = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        // dp[i][visited] : dp[현재 노드][지금까지 방문한 노드] = 나머지 정점을 이동하고 출발 정점으로 돌아오는데 걸리는 최소 비용
        dp = new int[N][1 << N]; 

        for (int i = 0; i < N; i++) {
            Arrays.fill(dp[i], 0); // dp 배열 초기화
        }

        int start = 0;
        int bit = 1;
        System.out.println(dfs(start, bit));
    }
}