/*
    2초, N<=10,000,000
    O(N) 사용해야 함 -> 자주 사용하는 투 포인터
*/

/*
    [연속된 자연수의 합] - 투 포인터
    시작 인덱스와 종료 인덱스를 지정해 연속된 수를 표현함
    - sum > N : sum = sum - start_index; start_index++;
    - sum < N : end_index++; sum = sum + end_index;
    - sum == N : end_index++; sum = sum + end_index; count++;
*/

/*
    N (연속된 자연수의 합)
    start_index = 1
    end_index = 1
    sum = 1     // 현제 연속된 합 값을 저장

    while(end_index != N){
        if sum==N: 경우의 수 증가, end_index 증가, sum값 변경
        else if(sum>N) sum값 변경, start_index 증가
        else if(sum<N) end_index 증가, sum값 변경
    }
*/

#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    int count = 1;
    int start_index = 1;
    int end_index = 1;
    int sum = 1;

    while (end_index != N){
        if (sum == N){
            count++;
            end_index++; sum += end_index;
        }
        else if (sum>N){
            sum -= start_index; start_index++; 
        }
        else{
            end_index++; sum += end_index;
        }
    }
    cout << count << "\n";

    return 0;
}