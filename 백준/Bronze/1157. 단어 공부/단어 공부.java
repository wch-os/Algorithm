import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        int[] frequency = new int[26];
        int alpha = System.in.read();

        while(alpha>='A'){
            if('a'<=alpha){
                frequency[alpha-'a']++;
            }
            else{
                frequency[alpha-'A']++;
            }

            alpha = System.in.read();
        }

        int max = -1;
        int index = 0;
        boolean duplicate = false;
        for(int i=0;i<26;++i){
            if(frequency[i]>max){
                max = frequency[i];
                index = i;
                duplicate = false;
            }
            else if(frequency[i]==max)
                duplicate = true;
        }

        if(duplicate)
            System.out.println('?');
        else
            System.out.println((char)('A'+index));

    }
}