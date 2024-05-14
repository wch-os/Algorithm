//perfect 뒤에 "." 안 붙임

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb= new StringBuilder();

        while(true){
            Queue<Integer> queue = new LinkedList<>();
            int N = Integer.parseInt(br.readLine());

            if(N==-1) //break 조건
                break;

            int sum = 0; //약수들의 합
            for(int i=1;i<N;++i){
                if(N%i==0) {
                    queue.add(i);
                    sum += i;
                }
            }

            if(N==sum){ //완전수이면, 오름차순으로 약수들의 합 출력
                sb.append(N).append(" = ").append(queue.poll());
                while(!queue.isEmpty()){
                    sb.append(" + ").append(queue.poll());
                }
                sb.append('\n');
            }
            else{ //완전수가 아니면
                sb.append(N).append(" is NOT perfect.").append('\n');
            }
        }

        System.out.println(sb);
    }
}