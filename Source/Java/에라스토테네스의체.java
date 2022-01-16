package Source.Java;

import java.util.*;

public class 에라스토테네스의체 {
    public static int n = 1000; // 2부터 1,000까지의 모든 수에 대하여 소수 판별
    public static boolean[] arr = new boolean[n+1];

    public static void findPrimes(){
        Arrays.fill(arr, true); // 처음엔 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)
       
        // 2부터 n 제곱근까지의 모든 수를 확인하며
        for(int i = 2;  i < Math.sqrt(n); i++){
            if(arr[i] == true){
                // i를 제외한 나머지 모든 배수를 지우기
                int j = 2;
                while (i * j <= n){
                    arr[i * j] = false;
                    j += 1;
                }
            }
        }
    }

    // 에라스토테네스의 체 원리 이용 (공간 복잡도 미사용)
    public boolean isPrime(int n){
        if(n==0 || n==1) return false;
        for(int i=3; i<=(int)Math.sqrt(n); i+=2){   // 통일 가능한 짝수 부분 제외
            if(n % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        findPrimes();   // 에라스토테네스의 체 알고리즘 수행

        // 모든 소수 출력
        for(int i = 2; i <= n; i++){
            if(arr[i]){
                System.out.print(i + " ");
            }
        }
    }
}
