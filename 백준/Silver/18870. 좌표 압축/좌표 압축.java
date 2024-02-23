import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //빠른 입력을 위해 버퍼를 이용해 입력을 받는다.

        int N = Integer.parseInt(br.readLine()); //수직선 위의 좌표의 개수를 입력받는다.

        ArrayList<Integer> list  = new ArrayList<>(N); //좌표 수만큼의 ArrayList 공간을 생성한다.


        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;++i){ //입력받은 값을 ArrayList에 저장한다.
            list.add(Integer.valueOf(st.nextToken()));
        }

        ArrayList<Integer> clone = (ArrayList<Integer>) list.clone();
        Collections.sort(clone); //오름차순으로 정렬한다.

        HashMap<Integer,Integer> map = new HashMap(N); //정렬한 좌표를 중복 없이 저장하기 위해 HashMap 구조를 사용한다.

        int rank = 0; //자신보다 작은 수가 몇 개 있는지
        for(int i=0;i<clone.size();++i){
            int input = clone.get(i); //정렬한 좌표에서 각 인덱스별로 추출하여 map 에 저장한다.
            if(!map.containsKey(input)) { //key : 좌표값, value : 순위 을 넣는다. //containsValue 를 검사하는 이유는 중복된 수 index 를 계산하지 않기 위함이다.
                map.put(input, rank);
                rank++; //순위를 올린다.
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i=0;i<N;++i){
            sb.append(map.get(list.get(i))).append(' '); //비정렬된(입력) 리스트 차례대로 값을 가지고 와 map - key 와 맞춰보며 순위를 찾는다.
        }

        System.out.println(sb); //순위를 출력한다.
    }
}