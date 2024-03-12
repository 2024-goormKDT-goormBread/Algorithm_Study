package algorithm.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_14501 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(reader.readLine());
        int[][] timeTable = new int[2][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            timeTable[0][i] = Integer.parseInt(st.nextToken());
            timeTable[1][i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(result(timeTable, n));
    }

    static int result(int[][] arr, int n) {
        int[] answer = new int[n + 1];
        int max = 0;

//        arr[0][i] -> 일 하는 시간
//        arr[1][i] -> 벌 수 있는 돈
//        work -> 이후에 일할 수 있는지 판단하기 위해
        for (int i = n - 1; i >= 0; i--) {

            int work = i + arr[0][i];

//            일할 수 있는 범위일 경우 점화식 적용
            if (work <= n) {
                answer[i] = Math.max(arr[1][i] + answer[arr[0][i] + i], max);
                max = answer[i];
            } else {
//                범위가 아닐 시 이전 요소를 저장
                answer[i] = max;
            }
        }
//        max = Arrays.stream(answer).max().orElseThrow();
//        return max;
        return answer[0];
    }
}
