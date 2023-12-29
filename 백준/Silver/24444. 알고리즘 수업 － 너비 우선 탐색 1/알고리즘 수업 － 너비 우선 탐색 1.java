import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<List<Integer>> graph; //graph 그리기 위한 인접 리스트
    static boolean visited[]; //각 정점 방문 여부 파악
    static int order[]; //각 정점이 몇 번째의 순서로 방문하는지 파악
    static int N,M,R;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        //기본 변수 초기화 (정점, 간선, 시작 정점, 클래스 자료구조..)
        init(br);

        //그래프 노드(정점) add + 각 노드 연결 간선 오름차순 정렬
        addEdge(br);

        //bfs 탐색
        bfs(R);

        //최종 출력
            //각 정점이 몇 번째로 순서로 방문하는지 출력
        for(int i=1;i<=N;++i){
            System.out.println(order[i]);
        }
    }
    
    private static void init(BufferedReader br) throws IOException {
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); //정점의 개수
        M = Integer.parseInt(st.nextToken()); //간선의 개수
        R = Integer.parseInt(st.nextToken()); //시작 정점

        graph = new ArrayList<>();
        for(int i=0;i<=N;++i){
            graph.add(new ArrayList<>());
        }
        visited = new boolean[N+1];
        order = new int[N+1];
    }

    private static void addEdge(BufferedReader br) throws IOException {
        StringTokenizer st;
        for(int i = 0; i<M; ++i){
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph.get(u).add(v); //그래프 양방향 간선 그리기
            graph.get(v).add(u);
        }

        for(List<Integer> inner : graph){ //내부 리스트 오름차순 정렬(!)
            Collections.sort(inner);
        }
    }

    private static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>(); //bfs 위한 FIFO 자료구조 사용
        queue.add(start); //queue에 add
        visited[start] = true; //시작 노드 방문 처리

        int count = 1; //각 정점 방문 순서(!) 체크

        while(!queue.isEmpty()){
            int front = queue.poll();

            order[front] = count; //정점 방문 순서 체크, 1등 2등...
            count++;

            for(int near : graph.get(front)){ //양 정점을 잇는 간선이 존재
                if(visited[near]==false){ //미방문 정점
                    queue.add(near); //queue에 추가
                    visited[near] = true; //방문 처리
                }
            }
        }
    }
}