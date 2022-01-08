package Algorithm.다이나믹프로그래밍;

import java.util.*;

// ai = i번째 식량창고까지의 최적의 해(얻을 수 있는 식량의 최댓값)
// ki = i번째 식량창고에 있는 식량의 양
// ai = max(a(i-1), a(i-2) + ki)

public class 개미전사 {
    // 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    public static int[] d = new int[100];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 정수 N을 입력 받기
        int n = sc.nextInt();

        // 모든 식량 정보 입력받기
        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        // 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
        d[0] = arr[0];
        d[1] = Math.max(arr[0], arr[1]);
        for (int i = 2;  i < n; i++){
            d[i] = Math.max(d[i-1], d[i-2] + arr[i]);
        }

        // 계산된 결과 출력
        System.out.println(d[n-1]);
    }
}

/*
입력 예시1
4
1 3 1 5
출력 예시1
8
*/