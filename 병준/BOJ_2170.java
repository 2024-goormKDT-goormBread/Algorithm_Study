package algorithm;
/*
문제 : 2170 선 긋기

선을 긋는 총 횟수를 입력받고
점의 위치를 입력받아 선의 총 길이를 출력

** 입력은 x가 y보다 작다는 것에 유의 **

 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_2170 {

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int pointCount = Integer.parseInt(reader.readLine());

        LinkedList<Point> points = new LinkedList<>();

//        LinkedList<int[]> points = new LinkedList<>();


        for (int i = 0; i < pointCount; i++) {
            st = new StringTokenizer(reader.readLine(), " ");

            points.add(new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));

//             리팩토링 전 입력문
//            int x = Integer.parseInt(st.nextToken());
//            int y = Integer.parseInt(st.nextToken());
//            int[] point = {x, y};
//            points.add(point);
        }

        Collections.sort(points, (p1, p2) -> Integer.compare(p1.x, p2.x));

//         리팩토링 전 x 정렬
//        points.sort(new Comparator<int[]>() {
//            public int compare(int[] x1, int[] x2) {
//                return Integer.compare(x1[0], x2[0]);
//            }
//        });

        Point comPoint = points.poll();
        int curX = comPoint.x;
        int curY = comPoint.y;
        int lengthSum = curY - curX;

        while (!points.isEmpty()) {
            Point nextPoint = points.poll();
            int nX = nextPoint.x;
            int nY = nextPoint.y;

//             리팩토링 전 조건문
//            if(curX <= nX && nY <= curY) {
//                continue;
//            } else if(nX < curY) {
//                lengthSum += nY - curY;
//            } else {
//                lengthSum += nY - nX;
//            }
//            curX = nX;
//            curY = nY;

            if (curY >= nX) { // 현재 선의 끝이 다음 선의 시작보다 클 때 (겹치거나 포함될 때)
                if (nY > curY) { // 다음 선의 끝이 현재 선의 끝보다 클 때만 길이를 더함
                    lengthSum += nY - curY;
                    curY = nY;
                }
            } else { // 현재 선과 다음 선이 겹치지 않을 때
                lengthSum += nY - nX;
                curX = nX;
                curY = nY;
            }
        }
        System.out.println(lengthSum);
    }
}
