package algorithm;
/*
push X: 정수 X를 큐에 넣는 연산
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력
size: 큐에 들어있는 정수의 개수를 출력
empty: 큐가 비어있으면 1, 아니면 0을 출력
front: 큐의 가장 앞에 있는 정수를 출력 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력
back: 큐의 가장 뒤에 있는 정수를 출력 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력

1.Queue 라이브러리엔 마지막 요소를 검색하는 메소드가 없어서 LinkedList 사용
2.출력하는데 사용한 StringBuilder는 시간초과 문제 해결을 위해 요소 저장 후 사용
3.push의 경우 스트링 배열로 만들어 1의 위치한 값을 형변환하여 저장

LinkedList 사용 메소드
- offer : 지정된 객체를 LinkedList의 끝에 추가
- poll : 첫 번째 요소 반환 후에 삭제
- size : 저장된 객체 수 반환
- isEmpty : 비어있는지 확인
- element : LinkedList 첫 번째 요소 반환
- getLast : LinkedList 마지막 요소 반환
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class BOJ_18258 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();
        LinkedList<Integer> queue = new LinkedList<>();
        int n = Integer.parseInt(reader.readLine());
        for (int i=0; i<n;i++){
            String inData = reader.readLine();
            String[] dataPart = inData.split(" "); // push의 경우 뒤 숫자를 받아오기 위함
            String checkData = dataPart[0];
            switch (checkData){
                case "push":
                    if (dataPart.length>1){
                        int pushNumber = Integer.parseInt(dataPart[1]);
                        queue.offer(pushNumber);
                        break;
                    }
                case "pop":
                    if (!queue.isEmpty()){
                        answer.append(queue.poll()+"\n");
                    }else {
                        answer.append("-1\n");
                    }
                    break;
                case "size":
                    answer.append(queue.size()+"\n");
                    break;
                case "empty":
                    if (!queue.isEmpty()){
                        answer.append("0\n");
                    }else{
                        answer.append("1\n");
                    }
                    break;
                case "front":
                    if (!queue.isEmpty()){
                        answer.append(queue.element()+"\n");
                    }else {
                        answer.append("-1\n");
                    }
                    break;
                case "back":
                    if (!queue.isEmpty()){
                        answer.append(queue.getLast()+"\n");
                    }else{
                        answer.append("-1\n");
                    }
                    break;
            }
        }
        System.out.println(answer);
        reader.close();
        System.out.println();
    }
}
