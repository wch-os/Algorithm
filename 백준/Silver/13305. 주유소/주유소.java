import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] cityDistance; //옆 도시까지의 거리
    static int[] oilPrice; //각 도시의 기름 가격
    static int cost = 0; //구하고자 하는 도시 이동 최소비용
    static int N, cl = 0; //현재 위치(currentLocation)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        cityDistance = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<N-1;++i){
            cityDistance[i] = Integer.parseInt(st.nextToken());
        }

        oilPrice = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;++i){
            oilPrice[i] = Integer.parseInt(st.nextToken());
        }

        solve();

        System.out.println(cost);
    }

    private static void solve() {
        //목적지(맨 오른쪽 도시)까지 도착할 때까지 반복
        while(cl!=N-1) {
            int co = oilPrice[cl]; //현재 도시의 기름 가격(currentOilPrice)
            int move = 0; //기름 가격을 고려해 현재 도시에서 기름을 구매해서 이동해야 하는 거리

            for (int i = cl + 1; i < N; ++i) {
                if (co >= oilPrice[i]) { //현재 위치보다 기름 가격이 싼 곳이 있다면 그 지점까지의 이동거리만큼만 구매한다.
                    for (int j = cl; j < i; ++j) {
                        move += cityDistance[j];
                    }

                    cost += co*move; //기름 구매
                    cl = i; //현재 위치 갱신
                    break; //인근 도시까지 이동 후 재탐색을 한다.
                }
            }
        }
    }
}