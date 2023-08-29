import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int count = 0;
        for(int i=0;i<N;++i){
            String word = br.readLine();

            if(solve(word))
                count++;
        }
        System.out.println(count);
    }

    private static boolean solve(String word) {
        boolean[] judge = new boolean[26];
        char prev = 0;
        for(char a : word.toCharArray()){
            if(prev!=a) {
                if(!judge[a - 'a']){
                    judge[a - 'a'] = true;
                    prev = a;
                }
                else{
                    return false;
                }
            }
        }
        return true;
    }
}