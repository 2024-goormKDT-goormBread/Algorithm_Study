package algorithm;
/*
문제 : 11501 주식
1. 주식 하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.

홍준이는 미래를 예상하는 뛰어난 안목을 가졌지만, 어떻게 해야 자신이 최대 이익을 얻을 수 있는지 모른다.
따라서 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.

홍준이의 행동 예

10 7 6 -> 10보다 큰 데이터가 없으므로 결과 값 0

3 5 9 -> 9가 가장 큰 데이터이므로 최대 값으로 지정 후 각 요소 뺌과 동시에 결과 저장 -> 10
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class BOJ_11501 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        List<Long> answer = new ArrayList<>();

        int testCase = Integer.parseInt(reader.readLine());

        for (int i = 0; i < testCase; i++) {
            // 날의 수 입력
            int test = Integer.parseInt(reader.readLine());

            // 각 날에 따른 주식 가격 입력
            String jusikInData = reader.readLine();
            String[] jusikData = jusikInData.split(" ");
            int[] jusik = new int[test];
            for (int j = 0; j < test; j++) {
                jusik[j] = Integer.parseInt(jusikData[j]);
            }

            // 최적 탐색
            long testResult = 0L;
            // 마지막 요소를 주식의 최대 값이라 설정
            int jusikMax = jusik[test-1];
            // 역순으로 탐색
            for (int j = test - 1; j >= 0; j--) {
                // 큰 시세 보다 작을 시 판매
                if (jusik[j] < jusikMax) {
                    testResult += jusikMax - jusik[j];
                }
                // 큰 시세로 지정
                else{
                    jusikMax = jusik[j];
                }
            }

            answer.add(testResult);
        }

        for(long num : answer) {
            System.out.println(num);
        }
    }
}
