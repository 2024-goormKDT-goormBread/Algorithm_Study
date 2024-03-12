package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1915 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            String line = reader.readLine();

            for (int j = 0; j < m; j++) {
                arr[i][j] = line.charAt(j) - '0';
            }
        }

        System.out.println(result(arr));
    }

    public static int result(int[][] arr) {
        int row = arr.length;
        int col = arr[0].length;

//        배열 탐색
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (arr[i][j] == 1) {
//                    점화식 적용
//                    왼쪽, 위, 대각석의 최솟값을 받아와 입력받은 배열에 저장
                    arr[i][j] += Math.min(Math.min(arr[i - 1][j], arr[i][j - 1]), arr[i - 1][j - 1]);
                }
            }
        }

//        스트림으로 최대값찾기
        int max = Arrays.stream(arr)
                .flatMapToInt(Arrays::stream)
                .max().orElseThrow();

//        forEach로 최대값 찾기
//        int max = 0;
//        for (int[] rows : arr) {
//            for (int value : rows) {
//                if (value > max) {
//                    max = value;
//                }
//            }
//        }

        return max * max;
    }
}
