package algorithm.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14889 {

    static int[][] ability;
    static boolean[] visited;
    static int n;
    static int minVal = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(reader.readLine());

        ability = new int[n][n];
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            for (int j = 0; j < n; j++) {
                ability[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0, 0);
        System.out.println(minVal);
    }

    public static void dfs(int i, int j) {
        if (j == n / 2){
            calDiff();
            return;
        }

        for (int k = i; k < n; k++) {
            if (!visited[k]) {
                visited[k] = true;
                dfs(k + 1, j + 1);
                visited[k] = false;
            }
        }
    }

    public static void calDiff(){
        int startTeam = 0, linkTeam = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i] && visited[j]) startTeam += ability[i][j];
                if (!visited[i] && !visited[j]) linkTeam += ability[i][j];
            }
        }

        int diff = Math.abs(startTeam - linkTeam);
        if (diff < minVal) {
            minVal = diff;
        }
    }

}
