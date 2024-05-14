import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        int i = 0;
        int j = str.length()-1;
        while(true){
            //양단에서 비교를 하면서 중앙까지 모두 비교했을 때
            //한글자 문자 또한, 해당 if 절을 넘어가면서 ++i,--j 되면서 통과된다.
            if(i>j) {
                System.out.println(1);
                break;
            }
            else if(str.charAt(i) != str.charAt(j)) {
                System.out.println(0);
                break;
            }

            ++i;
            --j;
        }
    }
}