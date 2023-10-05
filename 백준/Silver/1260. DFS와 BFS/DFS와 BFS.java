import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int graph[][];
    static boolean visited[];
    static int N,M,V;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); //정점의 개수
        M = Integer.parseInt(st.nextToken()); //간선의 개수
        V = Integer.parseInt(st.nextToken()); //시작할 정점의 번호

        graph = new int[N+1][N+1]; //그래프 양방향 간선 유무 파악
        visited = new boolean[N+1]; //그래프 정점 노드 방문 여부 파악

        for(int i=0;i<M;++i){
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a][b] = 1; //양방향 간선
            graph[b][a] = 1;
        }


        dfs(V);

        reset(); //방문 초기화

        bfs(V);

        System.out.println(sb);
    }

    private static void dfs(int start) {
        visited[start] = true; //방문 처리
        sb.append(start + " "); //dfs 방문 순서 저장

        for(int i=1;i<=N;++i){
            if(graph[start][i] == 1 && visited[i] == false){ //양 노드를 잇는 간선이 존재 + 미방문 노드일 경우
                dfs(i); //해당 노드를 중심으로 더 깊게 탐색하기
            }
        }
    }

    private static void reset() {
        for(int i=1;i<=N;++i){
            visited[i] = false;
        }

        sb.append('\n');
    }

    private static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start); //시작 노드 queue에 추가
        visited[start] = true; //방문 처리

        //queue가 빌 때가지 반복
        while(!queue.isEmpty()){
            int front = queue.poll();
            sb.append(front + " ");

            for(int i=1;i<=N;++i) {
                if (graph[front][i] == 1 && visited[i] == false) { //양 노드를 잇는 간선이 존재 + 미방문 노드일 경우
                    queue.add(i); //queue에 add 저장
                    visited[i] = true; //방문 처리
                }
            }
        }
    }
}