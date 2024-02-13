package algorithm;

import java.io.*;
import java.util.Stack;

public class Boj_10773 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(reader.readLine());
        Stack<Integer> S = new Stack<>();
        for (int i=0;i<N;i++){
            int A = Integer.parseInt(reader.readLine());
            switch (A){
                case 0:
                    S.pop();
                    break;
                default:
                    S.push(A);
                    break;
            }
        }
        int sum = 0;
        while(!S.isEmpty()) {
            sum += S.pop();
        }
        System.out.println(sum);
        reader.close();
        System.out.println();
    }
}
