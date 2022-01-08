package Algorithm.다이나믹프로그래밍;

import java.util.*;

// 가장 먼저 입력 받은 병사 정보의 순서를 뒤집습니다.
// 가장 긴 증가하는 부분 수열(LIS) 알고리즘을 수행하여 정답을 도출합니다.

public class 병사배치하기 {
    static int n;
    static ArrayList<Integer> v = new ArrayList<Integer>();
    static int[] dp = new int[2000];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 0; i < n; i++){
            v.add(sc.nextInt());
        }

        // 순서를 뒤집어 '최장 증가하는 부분 수열' 문제로 변환
        Collections.reverse(v);

        // 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
        for (int i = 0; i < n; i++){
            dp[i] = 1;
        }

        // 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
        for (int i = 1; i < n; i++){
            for (int j = 0; j < i; j++){
                if (v.get(j) < v.get(i)){
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        // 열외해야 하는 병사의 최소 수를 출력
        int maxValue = 0;
        for (int i = 0; i < n; i++){
            maxValue = Math.max(maxValue, dp[i]);
        }
        System.out.println(n - maxValue);
    }
}
 
/*
입력 예시1
7
15 11 4 8 5 2 4
출력 예시1
2
*/

/*
이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)로 알려진 전형적인 다이나믹 프로그래밍 문제의 아이디어와 같습니다.
예를 들어 하나의 수열 array = {4, 2, 5, 8, 4, 11, 15}이 있다고 합시다
- 이 수열의 가장 긴 증가하는 부분 수열은 {4, 5, 8, 11, 15} 입니다.
본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제로 치환할 수 있으며, LIS 알고리즘을 조금 수정하여 적용함으로써 정답을 도출할 수 있습니다.
*/

/*
가장 긴 증가하는 부분 수열(LIS)
D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
점화식: 모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
- 시간 복잡도: O(n^2)
*/