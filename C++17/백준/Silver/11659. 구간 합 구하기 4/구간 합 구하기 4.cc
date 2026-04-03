/*
    [line1]
    수의 개수 N (100,000 이하)
    합을 구해야 하는 횟수 M (100,000 이하)
    [line2]
    N개의 수
    [line3~]
    합을 구해야 하는 구간 i, j (M번) (i<=j<=N)

    ---

    numNo(숫자 개수), queryNo(합 횟수)
    S(합 배열)
    
    for(숫자 개수만큼){
        합 배열 생성(S[i] = S[i-1]+A)
    }
    for(합 횟수만큼){
        범위 받기 (i, j)
        부분 합 출력(S[j] - S[i-1])
    }

*/
// 1초, 100,000


#include <iostream>
using namespace std;

int main(){
    // 입출력 속도를 향상시키는 구문 추가
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int numNo; int queryNo;
    cin >> numNo >> queryNo;
    int S[100001]={};
    for (int i=1; i<=numNo; ++i){
        int temp;
        cin >> temp;
        S[i] = S[i-1] + temp;
    }
    for (int i=0; i<queryNo; ++i){
        int start, end;
        cin >> start >> end;
        cout << S[end]-S[start-1] << "\n";
    }
    return 0;
}