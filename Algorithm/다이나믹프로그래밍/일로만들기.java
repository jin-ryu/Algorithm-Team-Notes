package Algorithm.다이나믹프로그래밍;

import java.util.*;

// ai = i를 1로 만들기 위한 최소 연산 횟수
// ai = min(a(i-1), a(i/2), a(i/3), a(i/5)) + 1
// 단 1을 빼는 연산을 제외하고는 해당 수로 나누어 떨어질 때에 한해 점화식을 적용할 수 있습니다.

public class 일로만들기 {

    // 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    public static int[] d = new int[30001];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        // 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
        for (int i = 2; i <= x; i++){
            // 현재의 수에서 1을 빼는 경우
            d[i] = d[i-1] + 1;
            // 현재의 수가 2로 나누어 떨어지는 경우
            if (i%2 == 0){
                d[i] = Math.min(d[i], d[i/2] + 1);
            }
            // 현재의 수가 3로 나누어 떨어지는 경우
            else if (i%3 == 0){
                d[i] = Math.min(d[i], d[i/3] + 1);
            }
            // 현재의 수가 5로 나누어 떨어지는 경우
            else if (i%5 == 0){
                d[i] = Math.min(d[i], d[i/5] + 1);
            }
    
        }
        System.out.println(d[x]);
    }
}

/*
입력 예시1
26
출력 예시1
3
*/

/*
이 문제는 greedy로는 해결할 수 없다!
나누는 연산보다 빼는 연산으로 최솟값을 얻을 수도 있기 때문이다. 
(ex. 26에서 -1한 후 5로 2번 나눔 / 26에서 2로 먼저 나눔)
*/