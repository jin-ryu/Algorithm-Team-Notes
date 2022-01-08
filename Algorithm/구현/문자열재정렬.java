package Algorithm.구현;

import java.util.*
;
public class 문자열재정렬 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        ArrayList<Character> arrayList = new ArrayList<>();
        int num = 0;
        // 문자를 하나씩 확인하며
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            // 알파벳인 경우 결과 리스트에 삽입
            if(ch >= 'A' && ch <= 'Z'){
                arrayList.add(ch);
            }
            // 숫자는 따로 더하기
            else{
                
                num += ch - '0';
            }
        }
        // 알파벳을 오름차순으로 정렬
        Collections.sort(arrayList);
        
        String result = "";
        for(Character ch: arrayList){
            result += ch;
        }
        result += num;
        System.out.println(result);
    }
}

/*
입력 예시1
K1KA5CB7
입력 예시1
ABCKK13
입력 예시2
AJKDLSI412K4JSJ9D
출력 예시2
ADDIJJJKKLSS20
*/
