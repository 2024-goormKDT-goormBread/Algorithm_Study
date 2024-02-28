package algorithm;

/*
문제 : 나이트의 이동

입력의 첫째 줄에는 테스트 케이스의 개수룰 입력한다.
첫째 줄에는 체스판의 한 변의 길이를 입력한다. 체스판의 크기는 l × l이다.
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
둘째 줄은 나이트가 현재 있는 칸을 입력한다.
셋째 줄에는 나이트가 이동하려고 하는 칸을 입력한다.

각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

ex)
길이 3 현 위치 (2, 2) 이동 위치 (2, 1)
0 0 0 0    1 0 0 0     1 0 0 0
0 0 0 0 -> 0 0 0 0 ->  0 0 0 0
0 0 x 0    0 0 0 0     0 2 0 0
0 0 0 0    0 0 0 0     0 0 0 0
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_7562 {
    static int n;
    static int[][] board;
    static boolean[][] visited;
    // 8방향 이동 좌표
    static int[][] pos =
            {{-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}};
    static int nowX, nowY;
    static int desX, desY;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int test = Integer.parseInt(reader.readLine());

        for (int t = 0; t < test; t++) {
            n = Integer.parseInt(reader.readLine());

            board = new int[n][n];
            visited = new boolean[n][n];

            // 현재 나이트의 위치
            String nData = reader.readLine();
            String[] nXY = nData.split(" ");
            nowX = Integer.parseInt(nXY[0]);
            nowY = Integer.parseInt(nXY[1]);

            // 나이트가 이동할 위치
            String dData = reader.readLine();
            String[] dXY = dData.split(" ");
            desX = Integer.parseInt(dXY[0]);
            desY = Integer.parseInt(dXY[1]);

            visited[nowX][nowY] = true;
            bfs(nowX, nowY);
            System.out.println(board[desX][desY]);

        }
    }

    public static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        // 현 위치 추가
        queue.add(new int[]{x, y});

        while (!queue.isEmpty()) {
            // 값 삭제 후 반환
            int[] now = queue.poll();
            int nowX = now[0];
            int nowY = now[1];

            for (int i = 0; i < pos.length; i++) {
                int nX = nowX + pos[i][0];
                int nY = nowY + pos[i][1];

                if (nX < 0 || nX >= n || nY < 0 || nY >= n || visited[nX][nY] || board[nX][nY] != 0) {
                    continue;
                }

                visited[nX][nY] = true;
                board[nX][nY] = board[nowX][nowY] + 1;
                queue.add(new int[]{nX, nY});
            }
        }
    }
}
