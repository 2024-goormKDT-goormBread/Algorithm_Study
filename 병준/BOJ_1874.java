package algorithm;
// https://hongcoding.tistory.com/39
import java.io.*;
import java.util.Stack;

public class Boj_1874 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> S = new Stack<>();
        StringBuilder answer = new StringBuilder();
        int N = Integer.parseInt(reader.readLine());
        int checkNum = 0;
        boolean noYes = true;
        for (int i=0;i<N;i++){
            int Num = Integer.parseInt(reader.readLine());
            if (Num>checkNum) {
                for (int j = checkNum+1; j <= Num; j++) {
                    S.push(j);
                    answer.append("+\n");
                }
                checkNum = Num;
//                System.out.println(checkNum);
            } else if (S.peek()!=Num) {
                noYes = false;
            }
            S.pop();
            answer.append("-\n");
//            System.out.println(S);
        }
        if (noYes == true) {
            System.out.println(answer);
        }else {
            System.out.println("No");
        }
        reader.close();
        System.out.println();
    }
}
