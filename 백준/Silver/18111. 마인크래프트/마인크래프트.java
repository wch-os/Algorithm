// 풀이 시간 : 45분
// 시간복잡도 : O(256NM)
// 공간복잡도 : O(NM)
// 참고 : -

// 생각
    // 모든 땅을 고르게 한다.
    // min ~ max 까지 땅의 높이를 고르게 했을 때, 소요 시간을 파악한다.
    // 이전 소요 시간보다 크면 멈추고 출력 (최적화)

    // 시간을 계산한다.
    // if n > k (목표 높이가 높을 때)
        // n의 높이로 설정했을 때, n-k 쌓을 블록이 필요 → 1
    // elif n < k (목표 높이가 낮을 때)
        // k-n 블록을 제거 → 2

    // B + k-n < n-k
        // n 높이로 고르게 만드는 건 불가능

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M, B;
    static int min = Integer.MAX_VALUE; //주어진 땅 높이에서 최솟값
    static int max = Integer.MIN_VALUE; //주어진 땅 높이에서 최댓값

    static int[][] graph; // 모든 [i][j] 땅 높이 저장
    static int[] height = new int[257]; // 각 높이 [i]에 따른 소요 시간 저장


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        graph = new int[N][M];
        for (int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; ++j) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                min = Math.min(min, graph[i][j]);
                max = Math.max(max, graph[i][j]);
            }
        }

        Arrays.fill(height, Integer.MAX_VALUE); // 만들 수 없는 높이는 모두 MAX로 설정한다.
        for (int goal = min; goal <= max; ++goal) {
            int need = 0; // 메꿀 블록
            int push = 0; // 파야 할 블록
            for (int i = 0; i < N; ++i) {
                for (int j = 0; j < M; ++j) {
                    if (goal > graph[i][j]) {
                        need += (goal - graph[i][j]);
                    }
                    else if (goal < graph[i][j]) {
                        push += (graph[i][j] - goal);
                    }
                }
            }

            // (가지고 있는 블럭 + 메꿀 블럭 vs 파야 할 블록) 비교하여, 소요 시간 계산
            if (B + push >= need){
                height[goal] = push * 2 + need;
            }
        }

        // 땅을 고르는 데 걸리는 최소 소요 시간과 땅의 높이를 출력
        int resultMin = Integer.MAX_VALUE;
        int resultIdx = 0;
        for (int i = 0; i < height.length; ++i) {
            if (resultMin >= height[i]) {
                resultMin = Math.min(resultMin, height[i]);
                resultIdx = i;
            }
        }
        System.out.println(resultMin + " " + resultIdx);
    }
}