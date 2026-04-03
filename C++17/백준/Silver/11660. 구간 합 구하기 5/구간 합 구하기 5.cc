// 1초, 1<=N<=1024, 1<=M<=100,000
// 1억/500만/10,000/400~500

/*
    2차원 배열 구간 합
    D[X][Y] = (0,0) 부터 (X,Y)까지 사각형 영역의 합
    (1) 채우기
    D[1][j] = D[1][j-1] + A[1][j]
    D[i][1] = D[i-1][1] + A[i][1]
    (2) 채우기
    D[i][j] = D[i][j-1] + D[i-1][j]
              - D[i-1][j-1] + A[i][j]
    (3) 답 구하기
    (x1,y1) ~ (x2,y2) 까지의 합
    D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
*/

/*
    pseudo

    N(배열 크기), M(쿼리 수)
    A(원본 배열), D(합 배열)

    for (N만큼 반복){
        for (N만큼 반복){
            원본 배열 저장
        }
    }
    for (N만큼 반복){
        for (N만큼 반복){
            합 배열 저장
        }
    }
    for (M만큼 반복){
        쿼리 계산
    }
*/


#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<vector<int>> A(N+1, vector<int>(N+1,0));
    vector<vector<int>> D(N+1, vector<int>(N+1,0));

    for (int i=1; i<=N; ++i){
        for (int j=1; j<=N; ++j){
            cin >> A[i][j];
            D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j];
        }
    }
    for (int i=0; i<M; ++i){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1];
        cout << result << "\n";
    }
    return 0;
}