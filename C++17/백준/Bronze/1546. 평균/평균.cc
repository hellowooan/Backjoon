#include <iostream>
using namespace std;

/*
    N(시험 본 과목 개수) 입력 
    A(과목 데이터) 저장         (최대 1000개)

    for (N 만큼 반복){
        점수 데이터를 1차원 배열에 저장
    }
    for (배열 길이만큼 반복){
        최고점 점수 판별하여 저장
        총점 계산
    }
    sum * 100 / 최고점 / 과목수 출력

*/

#include <algorithm>
#include <vector>
int main(){
    int N; cin >> N;
    vector<int> scores(N);
    int total_sum=0;

    for (int i=0; i<N; ++i) cin >> scores[i];
    for (int s: scores) total_sum += s;
    int max_val = *max_element(scores.begin(), scores.end());
    double avg = (total_sum*100.00)/max_val/N;

    // 소수점 아래 2자리까지 고정
    cout << fixed;
    cout.precision(2);

    cout << avg << "\n";
    return 0;
}
