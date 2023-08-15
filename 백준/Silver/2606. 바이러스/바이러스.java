import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static ArrayList<Integer>[] graph;
    static boolean visited[];
    static int virus = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int edgeNum = Integer.parseInt(br.readLine());

        graph = new ArrayList[N + 1];
        visited = new boolean[N + 1];
        for(int i=0;i<N+1;++i){
            graph[i] = new ArrayList<Integer>();
        }

        for(int i=0;i<edgeNum;++i){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        //dfs(1);
        bfs(1);

        System.out.println(virus);
    }

    private static void dfs(int key) {
        visited[key] = true;

        for (int edge : graph[key]) {
            if(!visited[edge]){
                ++virus;
                dfs(edge);
            }
        }
    }

    private static void bfs(int key) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(key);
        visited[key] = true;
        while (!queue.isEmpty()) {
            int poll = queue.poll();
            //visited[poll] = true; //순회 그래프일 경우, 방문하자마자 visit 처리를 해야한다.
            for (int edge : graph[poll]) {
                if(!visited[edge]) {
                    ++virus;
                    visited[edge] = true;
                    queue.offer(edge);
                }
            }
        }
    }
}