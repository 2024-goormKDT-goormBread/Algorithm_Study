package algorithm;
/*
문제 : 쇠 막대기 (10799)
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ_10799 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String inData = reader.readLine();
        String[] data = inData.split("");
        Stack<Character> stack = new Stack<>();
        int answer = 0;
        for (int i = 0; i < data.length; i++) {
            if (data[i].equals("(")) stack.push('(');  // 여는 괄호는 스택에 추가
            else if (!stack.isEmpty() && data[i].equals(")")) {
                stack.pop();  // 닫는 괄호를 만나면 가장 최근의 여는 괄호를 스택에서 제거
                // 레이저를 감지합니다. 이전 문자가 여는 괄호인 경우, 레이저로 간주
                if (data[i - 1].equals("(")) {
                    answer += stack.size();
                    // 레이저에 의해 잘린 막대의 조각 수를 추가합니다. 스택의 크기는 현재 남아있는 막대의 수를 의미합니다.
                } else {
                    answer += 1;
                    // 레이저가 아닌 경우, 막대의 끝을 의미하므로 조각 수를 1만큼 증가시킵니다.
                }
            }
            System.out.print(answer);

        }
    }
}
