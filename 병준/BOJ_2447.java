package algorithm.boj;
/*
문제 : 2447 별 찍기 10

입력은 3의 제곱꼴의 수이다.
출력은 첫줄부터 n번 줄까지한다.

풀이

1. 패턴 분석

n = 3
***
* *
***

n = 9
*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********

공백은 (1,1) (1,4) (1,7)과
가운데 (3,3) (3,4) (3,5) ~ (5,3) (5,4) (5,5)의 규칙을 가진다.

(i / n) % 3 == 1 && (j / n) % 3 == 1 의 조건을 만족한다.

2. 재귀

조건문을 만족하면 별을 출력
그렇지 않으면 같은 과정을 반복한다.
그 과정은 작은 영역으로 나눠서 별 혹은 공백 출력

출력은 재귀를 돌때마다 System.in 메소드를 사용하면 시간초과가 발생하니
StringBuilder을 사용
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2447 {

    static StringBuilder answer = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                solution(i,j,n);
            }
//            System.out.println();
            answer.append("\n");
        }

        System.out.println(answer);
    }

    public static void solution(int i, int j, int n) {
        // 공백처리
        if ((i / n) % 3 == 1 && (j / n) % 3 == 1) {
//            System.out.print(" ");
            answer.append(" ");
        }
        else {
            if (n / 3 == 0) {
//                System.out.print("*");
                answer.append("*");
            } else {
                solution(i, j, n / 3);
            }
        }
    }
}
