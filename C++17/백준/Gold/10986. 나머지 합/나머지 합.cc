// 1<=N<=10^6, 2<=M<=1000
// 0<=Ai<=10^9

/*
    [나머지 합]
    (A+B)%C = ((A%C)+(B%C))%C

    구간 합 배열의 원소를 M으로 나눈 나머지를 업데이트하고,
    S[i]와 S[j]가 같은 (i,j)쌍을 찾으면,
    원본 배열에서 i+1~j까지의 구간 합
    (=S[j]-S[i])이 M으로 나누어진다.
*/

/*
// 아이디어: 구간 합의 나머지가 같을 경우, 나머지끼리 빼면 0이 된다.

N(숫자 개수), M(나머지 목표)
A(원본 배열), D(합 배열), C(같은 나머지를 가지는 인덱스 카운트)

for (i: 1~N)){
    원본 배열 채우기
    합 배열 결정
}
for (i: 0~N){
    remainder = D[i] % M
    if remainder == 0 : C[remainder]+1 
}
for (i: 0~M){
    C[i] (i를 나머지로 가지는 인덱스 개수)에서 2가지를 뽑는 경우의 수
    // C[i]개 중에 2개를 뽑는 경우의 수 계산 공식: C[i]*(C[i]-1)/2
}

*/

#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N; int M;
    cin >> N >> M;

    // int A[1000001]={};   // 불필요
    // long D[1000001]={};     // A가 10^9이므로 합배열은 10^15까지 커질 수 있음
    // int C[1001]={};

    vector<long long> D(N+1, 0);
    vector<long long> C(M, 0);
    long long result = 0;

    for (int i=1; i<=N; ++i){
        // cin >> A[i];
        // D[i] = D[i-1] + A[i];
        int temp = 0;
        cin >> temp;
        D[i] = D[i-1] + temp;

        int remainder;
        remainder = D[i] % M;
        C[remainder] += 1;
    }

    result += C[0];
    for (int i=0; i<M; ++i){
        result += C[i]*(C[i]-1)/2;
    }
    cout << result;
    return 0;
}