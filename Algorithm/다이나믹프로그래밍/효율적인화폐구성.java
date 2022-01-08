package Algorithm.다이나믹프로그래밍;

import java.util.*;

// ai = 금액 i를 만들 수 있는 최소한의 화페 개수
// k = 각 화폐의 단위
// 점화식: 각 화폐 단위인 k를 하나씩 확인하며
// a(i-k)를 만드는 방법이 존재하는 경우, ai = min(ai, a(i-k) + 1)
// a(i-k)를 만드는 방법이 존재하지 않는 경우, ai = INF

public class 효율적인화폐구성 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        // N개의 화폐 단위 정보를 입력 받기
        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        // DP 테이블 초기화
        int[] d = new int[m+1];
        Arrays.fill(d, 10001);

        // 다이나믹 프로기래밍(Dynamic Programming) 진행(보텀업)
        d[0] = 0;
        for (int i = 0; i < n; i++){
            for (int j = arr[i]; j <= m; j++){
                // (i-k)원을 만드는 방법이 존재하는 경우
                if(d[j - arr[i]] != 10001){
                    d[j] = Math.min(d[j], d[j - arr[i]] + 1);
                }
            }
        }
        if (d[m] == 10001){
            System.out.println(-1);
        }else{
            System.out.println(d[m]);
        }
    }
}

/*
입력 예시1
2 15
2
3
출력 예시1
5
입력 예시2
3 4
3
5
7
출력 에시2
-1
*/