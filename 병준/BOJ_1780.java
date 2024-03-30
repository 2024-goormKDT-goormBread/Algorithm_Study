package algorithm.boj;
/*
문제 : 1780 종이의 개수

종이를 9등분해서 각 -1,0,1으로 이뤄진 종이의 개수를 센다.
한 구역 내에 같은 숫자로 이뤄지지 않으면 9등분한다.

풀이

1. 해당 구역에 같은 색상이 있는지 판단한다.
2. 같은 색상이면 answer 배열에 값을 더한다.
3. 만약 같지 않다면 subAnswer 배열 재귀 호출을 마쳐 각 값을 더한다.
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1780 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        int[][] arr = new int[n][n];
        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int num : solution(0, 0, n, arr)) {
            System.out.println(num);
        }
    }

    public static int[] solution(int x, int y, int n, int[][] arr) {
        int[] answer = new int[3];
        boolean sameData = true;
        int firstValue = arr[x][y];

        for (int i = x; i < x + n; i++) {
            for (int j = y; j < y + n; j++) {
                if (arr[i][j] != firstValue) {
                    sameData = false;
                    break;
                }
            }
            if (!sameData) break;
        }

        if (sameData) {
            answer[firstValue + 1] += 1;
            return answer;
        }
        else {
            int z = n / 3;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int[] subAnswer = solution(x + i * z, y + j * z, z, arr);

                    for (int k = 0; k < 3; k++) {
                        answer[k] += subAnswer[k];
                    }
                }
            }
        }
        return answer;
    }
}
