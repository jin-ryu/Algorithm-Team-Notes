package Algorithm.구현;

import java.util.*;

public class 상하좌우 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N을 입력 받기
        int n = sc.nextInt();
        sc.nextLine();  // 버퍼 지우기
        String[] plans = sc.nextLine().split(" ");
        int x = 1, y = 1;

        // L, R, U, D에 따른 이동 방향
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        char[] moveTypes = {'L', 'R', 'U', 'D'};

        // 이동 계획을 하나씩 확인
        for(int i = 0; i < plans.length; i++){
            char plan = plans[i].charAt(0); // plans가 String 배열이므로 charAt으로 첫번째 문자 뽑음
            // 이동 후 좌표 구하기
            int nx = -1, ny = -1;
            for(int j = 0; j < 4; j++){
                if(plan == moveTypes[j]){
                    nx = x + dx[j];
                    ny = y + dy[j];
                }

                // 공간을 벗어나는 경우 무시
                if(nx < 1 || ny < 1 || nx > n || ny > n) continue;
                // 이동 수행
                x = nx;
                y = ny;
            }
        }

        System.out.println(x + " " + y);
    }
}

/* 
입력 예시1
5
R R R U D D
출력 예시1
3 4
*/