import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] ary;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        //주어진 정수 개수
        int N = Integer.parseInt(br.readLine());
        ary = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;++i){
            ary[i] = Integer.parseInt(st.nextToken());
        }

        //이분탐색을 위한 오름차순 정렬
        Arrays.sort(ary);

        //비교할 정수 개수
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<M;++i){
            int num = Integer.parseInt(st.nextToken());
            boolean search = binary_search(num);
            if(search)
                sb.append(1).append('\n');
            else
                sb.append(0).append('\n');
        }
        System.out.println(sb);
    }

    private static boolean binary_search(int num) {
        int start = 0;
        int end = ary.length-1;

        while(start<=end){
            int mid = (start + end) / 2;

            if(ary[mid] == num)
                return true;
            else{
                if(ary[mid]<num)
                    start = mid+1;
                else
                    end = mid-1;
            }
        }

        return false;
    }
}