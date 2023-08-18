import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] graph;
    static int[] visited;
    static StringBuilder sb = new StringBuilder();
    static int order = 1; //방문순서 체크

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); //정점의 개수
        int M = Integer.parseInt(st.nextToken()); //간선의 개수
        int R = Integer.parseInt(st.nextToken()); //시작 정점

        graph = new ArrayList[N+1];
        visited = new int[N+1];

        for (int i = 0; i < N+1; ++i) {
            graph[i] = new ArrayList();
        }

        //무방향 그래프
        for (int i = 0; i < M; ++i) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            graph[start].add(end);
            graph[end].add(start);
        }

        //인접 정점은 내림차순으로 방문한다.
        for (int i = 0; i < N+1; ++i) {
            Collections.sort(graph[i], Collections.reverseOrder());
        }

        //dfs 탐색 (시작 정점, 방문 순서)
        dfs(R);

        //각 노드 방문 순서 출력
        for(int i=1;i<N+1;++i) {
            sb.append(visited[i]).append('\n');
        }
        System.out.println(sb);
    }

    private static void dfs(int start) {
        visited[start] = order++;

        for (int e : graph[start]) {
            //미방문 노드일 경우, dfs 탐색
            if(visited[e] == 0) {
                dfs(e);
            }
        }
    }
}