package Source.Java;

import java.util.*;

class Fruit implements Comparable<Fruit> {
    private String name;
    private int score;

    public Fruit(String name, int score){
        this.name = name;
        this.score = score;
    }

    public String getName(){
        return this.name;
    }

    public int getScore(){
        return this.score;
    }

    // 정렬 기준은 '점수가 낮은 순서'
    @Override
    public int compareTo(Fruit o) {
        // TODO Auto-generated method stub
        if(this.score < o.score){   // 역순으로 할때는 괄호 방향을 바꾸면 됨
            return -1;  
        }
        return 1;
    }
}

public class 정렬라이브러리예제 {

    // 정렬 라이브러리 기본 예제
    public static void basicSort(){
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        // 배열 정렬
        Arrays.sort(arr);

        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
    }

    // 정렬 라이브러리 기본 예제(위에서 아래로)
    public static void basicSortReverseOrder(){
        Integer[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        // 배열 정렬 (int가 아닌 Integer 형태의 배열이어야 함)
        Arrays.sort(arr, Collections.reverseOrder());

        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
    }

    // 정렬 라이브러리 키(Key) 기준 정렬 예제
    public static void keySort(){
        List<Fruit> fruits = new ArrayList<>();

        fruits.add(new Fruit("바나나", 2));
        fruits.add(new Fruit("사과", 5));
        fruits.add(new Fruit("당근", 3));

        // 리스트 정렬
        Collections.sort(fruits);

        for (int i = 0; i < fruits.size(); i++){
            System.out.print("(" + fruits.get(i).getName() + ", " +  fruits.get(i).getScore() + ") ");
        }
    }

    public static void main(String[] args) {
        basicSort();
        System.out.println();

        basicSortReverseOrder();
        System.out.println();

        keySort();
    }
}
