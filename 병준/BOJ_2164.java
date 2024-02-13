package algorithm;
/*
1.Queue 라이브러리엔 마지막 요소를 검색하는 메소드가 없어서 LinkedList 사용
2.첫 번째 요소를 삭제 후 그 다음 요소를 poll()을 이용해 값을 반환하고 삭제
3.삭제한 요소를 offer()을 이용해 마지막으로 삽입

LinkedList 사용 메소드
- offer : 지정된 객체를 LinkedList의 끝에 추가
- poll : 첫 번째 요소 반환 후에 삭제
- peek : 첫 번째 요소 반환
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class BOJ_2164 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        LinkedList<Integer> card = new LinkedList<>();
        int n = Integer.parseInt(reader.readLine());
        for (int i = 1;i<=n;i++){
            card.offer(i);
        }
        while (card.size()>1){
            card.poll();
            card.offer(card.poll());
        }
        System.out.println(card.peek());
    }
}
