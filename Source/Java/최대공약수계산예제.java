package Source.Java;

public class 최대공약수계산예제 {
    
    // 유클리드 호제법: gcd(A, B) ==  gcd(B, A % B)
    public static int gcd(int a, int b){
        if(a % b == 0)
            return b;
        return gcd(b, a % b);
    }
    public static void main(String[] args) {
        System.out.println(gcd(192, 162));  // 6
    }
}
