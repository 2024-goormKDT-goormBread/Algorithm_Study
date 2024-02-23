package algorithm;
/*
문제 : 적록색약 10026번
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_10026 {
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,1,-1}; // 상하좌우 탐색을 위해 선언
    static boolean[][] visit; // 탐색을 위해 선언
    static String[][] data;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        data = new String[n][n];
        visit = new boolean[n][n];

        for (int i=0;i<n;i++){
            String inData = reader.readLine();
            String[] color = inData.split("");
            for (int j=0;j<n;j++){
                data[i][j] = color[j];
            }
        }

        // 일반인이 판단할 수 있는 구역
        int nomalCnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visit[i][j]) {
                    bfs(i, j,n);
                    nomalCnt++;
                }
            }
        }

        // 적록색약 환자가 판단할 수 있는 구역
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                if (data[i][j].equals("G")){
                    data[i][j] = "R";
                }
            }
        }
        int cnt = 0;
        // 적록색약을 다시 판단하기 위해 초기화
        visit = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visit[i][j]) {
                    bfs(i, j,n);
                    cnt++;
                }
            }
        }
        System.out.println(nomalCnt+" "+cnt);
    }
    public static void bfs(int x,int y, int n){
        Queue<int []> queue = new LinkedList<>();
        // x,y는 현재 좌표를 의미 ex) (0,0) , (3,0) ...
        queue.offer(new int[]{x,y});
        // 현재 좌표를 방문했기에 true
        visit[x][y] =true;
        // 현재 좌표의 색상
        String color = data[x][y];

        // 같은 색상인지 판단을 위해 큐가 비어있을 때까지
        while (!queue.isEmpty()){
            // 현재 위치한 x,y의 좌표 초기화
            int[] cur = queue.poll();
            int curX = cur[0], curY = cur[1];

            // 상화좌우 탐색
            for (int i=0;i<4;i++){
                // ex) cur이 (3,3) 경우
                // i = 0 -> nX = 3-1=2, nY = 3+0=3
                // ...
                // i = 3 -> nX = 3-0=0, nY = 3-1=2
                int nX = curX + dx[i];
                int nY = curY + dy[i];

                // 인덱스 범위가 0~ n-1이므로 유효성 검사
                // 방문여부와 같은 색상인지 판단
                if (nX>=0&& nX<n && nY>=0 && nY<n && !visit[nX][nY] && data[nX][nY].equals(color)){
                    visit[nX][nY] = true;
                    queue.offer(new int[]{nX,nY});
                }
            }
        }
    }
}
