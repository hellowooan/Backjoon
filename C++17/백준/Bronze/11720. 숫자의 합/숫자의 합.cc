#include <iostream>
#include <vector>
using namespace std;

/*
    [명시적 형변환]
    stoi(string)    int
    stol(string)    long
    stod(string)    double
    stof(string)    float

    to_string(int, long, double, float)

    [암시적 형변환]
    작은 타입과 큰 타입이 계산하면 큰 타입으로 맞춰진다.
    int 연산을 할 경우, char는 아스키 코드로 변환됨
*/

// N의 범위가 1~100까지 이므로, int, long으로 담을 수 없음
// 문자열로 받고 이를 숫자로 치환

/*
    슈도 코드
    N값 받기
    숫자를 string 변수(numbers)로 입력받기
    sum 변수 선언
    for (numbers만큼 반복){
        sum에 배열의 각 자리 값을 정수화해서 더하기
    }
    sum 출력
*/

int main(){
    int N; 
    string numbers; 

    cin >> N;
    cin >> numbers;

    int sum = 0;
    for (int i = 0; i<numbers.length(); ++i){
        // 문자의 ascii 값을 연산
        sum += numbers[i] - '0';
    }
    cout << sum << endl;
    return 0;
}