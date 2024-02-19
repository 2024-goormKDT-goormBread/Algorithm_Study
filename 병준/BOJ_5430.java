package algorithm;
/*
 * 문제 : AC [5430]
 * 풀이 : 특정 함수에 맞게 커맨드 실행
 *       R -> 함수 뒤집기
 *       D -> 첫 번째 요소 삭제
 *
 * 문제사항 및 해결
 * 1. 시간초과
 *    기존 코드에 많은 변수 선언 및 "R" 명령어를 처리할 때 실제로 리스트를 뒤집는 대신, 뒤집힌 상태를 표시하는 플래그를 사용할 수 있었습니다.
 *    실제 뒤집기 연산은 필요할 때만(즉, 요소에 접근하거나 결과를 출력할 때만) 수행하도록 했습니다.
 *    뒤집힌 상태를 관리하는 불리언 변수를 사용하여, 리스트가 현재 뒤집힌 상태인지 아닌지를 추적합니다.
 *    최종 결과를 출력할 때만 실제로 리스트의 순서를 조정하거나, 뒤집힌 상태를 기반으로 조건적으로 요소를 출력했습니다.
 * 2. 런타임에러 (NumberFormat)
 *    inArr을 가져올 때 readLine()을 두 번 호출하는 대신, 한 번만 호출하도록 수정했습니다.
 *
 * */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;

public class BOJ_5430 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(reader.readLine());
        for (int i=0;i<testCase;i++){
            String functions = reader.readLine();
//            String[] func = functions.split("");
            int arrLength = Integer.parseInt(reader.readLine());
//            String inArr = reader.readLine().substring(1, reader.readLine().length() - 1);
            String inArr = reader.readLine(); // 한 번만 호출하도록 수정
            inArr = inArr.substring(1, inArr.length() - 1);
            String[] test = inArr.split(",");
//            LinkedList<String> funcList = new LinkedList<>();
            LinkedList<Integer> arrList = new LinkedList<>();
            boolean ansBool = true;
            boolean isReversed = false;

            for (int j = 0; j < arrLength; j++) {
                arrList.offer(Integer.parseInt(test[j]));
            }

            for (char func : functions.toCharArray()) {
                if (func == 'R') {
                    isReversed = !isReversed;
                } else if (func == 'D') {
                    if (arrList.isEmpty()) {
                        ansBool = false;
                        break;
                    }
                    if (isReversed) {
                        arrList.removeLast();
                    } else {
                        arrList.removeFirst();
                    }
                }
            }

            if (ansBool) {
                if (isReversed) {
                    Collections.reverse(arrList);
                }
                StringBuilder ans = new StringBuilder("[");
                while (!arrList.isEmpty()) {
                    ans.append(arrList.poll()).append(",");
                }
                if (ans.length() > 1) {
                    ans.setLength(ans.length() - 1);
                }
                ans.append("]");
                System.out.println(ans);
            } else {
                System.out.println("error");
            }
//            boolean ansBool = true;       // 기존 코드 시작
//            for (int j=0;j<func.length;j++){
//                funcList.offer(func[j]);
//            }
//            for (int j=0;j<arrLength;j++){
//                arrList.offer(Integer.parseInt(test[j]));
//            }
//            while (!funcList.isEmpty()){
//                String lunchFunc = funcList.removeFirst();
//                if (!arrList.isEmpty()) {
////                    int arrSize = arrList.size();
//                    switch (lunchFunc) {
//                        case "R":
//                            Collections.reverse(arrList);
////                            for (int k = 0;k<arrSize/2;k++){
////                                Integer temp = arrList.get(k);
////                                arrList.set(k,arrList.get(arrSize-1-k));
////                                arrList.set(arrSize-1-k,temp);
////                            }
//                            break;
//                        case "D":
//                            arrList.pop();
//                            break;
//                    }
//                }else{
//                    ansBool = false;
//                }
//            }
//            if (ansBool == true) {
//                StringBuilder ans = new StringBuilder("[");
//                int ansListLength = arrList.size();
//                for (int k = 0; k < ansListLength; k++) {
//                    ans.append(arrList.poll()).append(",");
//                }
//                ans.setLength(ans.length() - 1);
//                ans.append("]");
//                System.out.println(ans);
//            }else {
//                System.out.println("error"); // 기존 코드 끝
//            }
        }
    }
}