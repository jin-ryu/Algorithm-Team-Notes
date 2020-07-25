#[?] 무작위 데이터를 순서대로 [오름차순(ASC)|내림차순(DESC)] 정렬 

def main():
    #[1] Input
    numbers = [3, 2, 1, 5, 4]
    N = len(numbers)

    #[2] Process: Bubble Sort(거품 정렬) 알고리즘
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j+1], numbers[j]
    #[2] Output
    for i in range(len(numbers)):
        print(numbers[i], end = "\t")
    print()

if __name__ == "__main__":
    main()

#[!] Bubble Sort
# 서로 인접한 두 원소를 비교하여 정렬하는 알고리즘
# 데이터 개수가 n개이면 전체 회전수는 n-1회
# 오름차순 기준으로 매 회전마다 가장 큰 데이터가 배열의 끝으로 이동 