package Algorithm.구현;

import java.util.*;

public class 왕실의나이트 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 현재 나이트의 위치 입력받기
        String knight = sc.nextLine();
        int x = knight.charAt(1) - '0';
        int y = knight.charAt(0) - 'a' + 1;
        
        // 나이트가 이동할 수 있는 8가지 방향 정의
        int[] dx = {-2, -2, 2, 2, 1, 1, -1, -1};
        int[] dy = {-1, 1, -1, 1, -2, 2, -2, 2};
    
        // 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
        int cnt = 0;
        for(int i = 0;  i < dx.length ; i++){
            // 이동하고자 하는 위치 확인
            int nx = x + dx[i];
            int ny = y + dy[i];
            // 해당 위치로 이동이 가능하다면 카운트 증가
            if(nx >= 1 && nx <= 8 && ny >= 1 && ny <= 8)
                cnt++;
        }
        System.out.println(cnt);
    }
}

/*
입력 예시1
a1
출력 예시1
2
입력 예시2
c2
출력 예시2
6
*/