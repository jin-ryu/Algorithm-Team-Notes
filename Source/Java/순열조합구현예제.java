package Source.Java;

import java.util.*;

public class 순열조합구현예제 {
    public static int[] arr = {1, 2, 3, 4, 5};

    /*
    순열 구현 코드
    - r: 뽑고자 하는 개수    
    - temp: r개를 뽑은 결과값을 저장해놓은 배열
    - current: 현재 개수를 저장해 놓는 값
    - visited: 방문 여부를 확인하는 배열
    */
    public static void makePermutation(int r, int[] temp, int current, boolean[] visited){
        if(r == current){   
            // r개의 수를 선택했다면 출력
            System.out.println(Arrays.toString(temp));
        }else{
            for(int i = 0; i < arr.length;  i++){
                if(!visited[i]){
                    visited[i] = true;  // 아직 방문하지 않았다면 방문 처리
                    temp[current] = arr[i]; // 방문한 숫자를 결과에 추가
                    makePermutation(r, temp, current + 1, visited); // 다음에 방문할 숫자 탐색
                    visited[i] = false; // 방문 처리 해제
                }
            }
        }
    }

    /*
    조합 구현 코드
    - r: 뽑고자 하는 개수
    - temp: r개를 뽑은 결과값을 저장해놓은 배열
    - current: 현재 개수를 저장해 놓는 값
    - start: 그 다음 반복문을 시작하는 값
    */ 
    public static void makeCombination(int r, int[] temp, int current, int start){
        if(r == current){
            // r개의 수를 선택했다면 출력
            System.out.println(Arrays.toString(temp));
        }else{
            for (int i = start; i < arr.length; i++){   // 이미 선택한 대상을 제외하기 위해 start 인덱스 부터 순회
                temp[current] = arr[i];
                makeCombination(r, temp, current + 1, i + 1);
            }
        }
    }

    /*
    중복순열 소스코드
    - r: 뽑고자 하는 개수    
    - temp: r개를 뽑은 결과값을 저장해놓은 배열
    - current: 현재 개수를 저장해 놓는 값
    */
    public static void makeOverlapPermutation(int r, int[] temp, int current){
        if(r == current){
            System.out.println(Arrays.toString(temp));
        }else{
            for(int i = 0; i < arr.length; i++){
                // 중복 순열은 숫자가 중복되어도 되기 때문에 visited 배열이 필요 없다
                temp[current] = arr[i];
                makeOverlapPermutation(r, temp, current + 1);
            }
        }
    }

    /*
    중복조합 소스코드
    - r: 뽑고자 하는 개수
    - temp: r개를 뽑은 결과값을 저장해놓은 배열
    - current: 현재 개수를 저장해 놓는 값
    - start: 그 다음 반복문을 시작하는 값
    */
    public static void makeOverlapCombination(int r, int[] temp, int current, int start){
        if(r == current){
            System.out.println(Arrays.toString(temp));
        }else{
            for(int i = start; i < arr.length; i++){
                temp[current] = arr[i];
                makeOverlapCombination(r, temp, current + 1, i);    // 중복 조합이므로 현재 선택한 값이 또 나올 수 있게 start 인덱스를 유지
            }
        }
    }

    public static void main(String[] args) {
        int r = 3;  // 뽑고자 하는 개수

        // 순열 출력하기
        System.out.println("순열 출력하기");
        makePermutation(r, new int[r], 0, new boolean[arr.length]);
        // 조합 출력하기
        System.out.println("조합 출력하기");
        makeCombination(r, new int[r], 0, 0);

        // 중복순열 출력하기
        System.out.println("중복순열 출력하기");
        makeOverlapPermutation(r, new int[r], 0);
        // 중복조합 출력하기
        System.out.println("중복조합 출력하기");
        makeOverlapCombination(r, new int[r], 0, 0);
    }
}
