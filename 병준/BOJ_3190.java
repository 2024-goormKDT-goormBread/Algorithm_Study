package algorithm.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BOJ_3190 {

    static LinkedList<Position> snake = new LinkedList<>();
    static LinkedList<Move> moves = new LinkedList<>();
    static int n;
    static int[][] board;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    // 해결 코드
    public static int solution() {
        int time = 0;
        int dir = 0;
        snake.add(new Position(0, 0));
        while (true) {
            if (!moves.isEmpty() && time == moves.peek().sec) {
                dir = changeDirection(dir, moves.poll().dire);
            }

            int nx = snake.getLast().x + dx[dir];
            int ny = snake.getLast().y + dy[dir];

            if (isGameSet(nx, ny)) {
                return time + 1;
            }

            if (nx >= 0 && ny >= 0 && nx < n && ny < n && board[nx][ny] == 1) {
                board[nx][ny] = 0;
            } else {
                snake.poll();
            }

            snake.add(new Position(nx, ny));
            time++;
            /*
            for (Position position : snake) {
                System.out.println(position);
            }
            */
        }
    }

    // 게임 종료
    public static boolean isGameSet(int nx, int ny) {
        return nx < 0 || ny < 0 || nx >= n || ny >= n || contains(snake, nx, ny);
    }

    // 방향 전환
    public static int changeDirection(int current, char turn) {
        if (turn == 'L') {
            return (current + 3) % 4;
        } else if (turn == 'D') {
            return (current + 1) % 4;
        }
        return current;
    }

    // 현 위치가 뱀의 일부를 판단
    public static boolean contains(LinkedList<Position> snake, int x, int y) {
        for (Position pos : snake) {
            if (pos.x == x && pos.y == y) return true;
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(reader.readLine());
        board = new int[n][n];

        int k = Integer.parseInt(reader.readLine());
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            board[x][y] = 1;
        }

        int l = Integer.parseInt(reader.readLine());
        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            int sec = Integer.parseInt(st.nextToken());
            char dire = st.nextToken().charAt(0);
            moves.add(new Move(sec, dire));
        }

        System.out.println(solution());
    }

    static class Position {
        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Move {
        int sec;
        char dire;

        public Move(int sec, char dire) {
            this.sec = sec;
            this.dire = dire;
        }
    }
}
