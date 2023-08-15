import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Pair implements Comparable<Pair>{
    int distance;
    int startPoint;

    public Pair(int distance, int startPoint) {
        this.distance = distance;
        this.startPoint = startPoint;
    }

    @Override
    public int compareTo(Pair other) {
        return Integer.compare(this.distance, other.distance);
    }
}

public class Main {
    static ArrayList<Pair>[] graph;
    static int[] minCost;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine()); //도시의 개수
        int M = Integer.parseInt(br.readLine()); //버스의 개수

        graph = new ArrayList[N+1];
        minCost = new int[N+1];
        Arrays.fill(minCost, Integer.MAX_VALUE); //도시까지 가는 경로 Max로 초기화

        for(int i=0;i<graph.length;++i){
            graph[i] = new ArrayList();
        }

        for(int i=0;i<M;++i){
            st = new StringTokenizer(br.readLine());
            //출발지 인덱스에 도착지, 비용 저장

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            if(start == end)
                continue;

            graph[start].add(new Pair(cost, end));
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        dijkstra(start);

        System.out.println(minCost[end]);
    }

    private static void dijkstra(int start) {
        PriorityQueue<Pair> q = new PriorityQueue<>();
        q.offer(new Pair(0, start));

        while (!q.isEmpty()){
            Pair poll = q.poll();

            if (minCost[poll.startPoint] < poll.distance) //지금까지의 최소거리가 아니면 무시하기
                continue;

            for(Pair next : graph[poll.startPoint]){ //현재 지점과 연결된 간선 정보 불러오기
                int sum = poll.distance + next.distance; //현재 지점까지의 비용 + 다음 도시까지의 비용
                if(minCost[next.startPoint] > sum){ //비용 갱신
                    minCost[next.startPoint] = sum;
                    q.offer(new Pair(sum, next.startPoint));
                }
            }
        }
    }
}