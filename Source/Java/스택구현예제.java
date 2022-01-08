package Source.Java;

import java.util.*;

public class 스택구현예제 {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        
        // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
        s.push(5);
        s.push(2);
        s.push(3);
        s.push(7);
        s.pop();
        s.push(1);
        s.push(4);
        s.pop();

        // 스택의 최상단 원소부터 출력
        while(!s.isEmpty()){
            System.out.println(s.peek() + " ");
            s.pop();    // 실행 결과 : 1 3 2 5
        }
    }    
}
