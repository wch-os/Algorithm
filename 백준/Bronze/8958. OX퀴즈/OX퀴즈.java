import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        for(int i=0;i<T;++i){
            String quiz = br.readLine();
            int count = 0;
            int sum = 0;
            for(char answer : quiz.toCharArray()){
                if(answer=='O')
                    count++;
                else
                    count=0;
                sum += count;
            }
            System.out.println(sum);
        }
    }
}