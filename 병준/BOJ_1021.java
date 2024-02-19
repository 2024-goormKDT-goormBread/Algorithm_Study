package algorithm;
/*
* 문제 : 회전하는 큐 [1021]
* 풀이 : 1 연산 : 첫 번째 요소 삭제
*       2 연산 : 왼쪽으로 한 칸 이동
*       3 연산 : 오른쪽으로 한 칸 이동
*       2,3 연산만 answer 값을 증가시켜 입력한 요소가 다 삭제되면 출력
*
*       2,3 연산은 최솟값으로 해야하기에 리스트 크기의 반을 잘라 어느 연산 사용할지 판단
* */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class BOJ_1021 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] inNM = reader.readLine().split(" ");
        int n = Integer.parseInt(inNM[0]);
        int m = Integer.parseInt(inNM[1]);
        String[] inArr = reader.readLine().split(" ");
        int[] arr = new int[m];
        for (int i = 0; i<m;i++){
            arr[i] = Integer.parseInt(inArr[i]);
        }
        LinkedList<Integer> list = new LinkedList<>();
        for (int i=1;i<=n;i++){
            list.offer(i);
        }
        int ans = 0;
        for (int i=0;i<m;i++){
            int deleteElement = list.indexOf(arr[i]);
            int middleArea;
//            System.out.println(deleteElement);
            if (list.size()%2==0){
                middleArea = list.size()/2 -1;
            }
            else {
                middleArea = list.size() / 2;
            }
//            System.out.println(middleArea);
            if (deleteElement<=middleArea){
                for (int k =0;k<deleteElement;k++){
                    list.offer(list.poll());
                    ans++;
//                    System.out.println(list);
                }
            }else {
                for (int k = 0; k<list.size()-deleteElement;k++){
                    list.offerFirst(list.pollLast());
                    ans++;
//                    System.out.println(list);
                }
            }
            list.pop();
        }
        System.out.println(ans);
    }
}