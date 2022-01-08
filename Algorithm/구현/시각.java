package Algorithm.구현;

import java.util.*;

public class 시각 {
    
    // 특정한 시각 안에 '3'이 포함되어 있는지의 여부
    public static boolean check(int h, int m, int s){
        if(h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3)
            return true;
        return false;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // N을 입력 받기
        int n = sc.nextInt();
        int cnt = 0;

        for(int h = 0; h <= n; h++){
            for(int m = 0; m < 60; m++){
                for(int s = 0; s < 60; s++){
                    // 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                    if(check(h, m, s)) cnt++;
                }
            }
        }
        System.out.println(cnt);
    }
}

/*
입력 예시1
5
출력 예시1
11475
*/