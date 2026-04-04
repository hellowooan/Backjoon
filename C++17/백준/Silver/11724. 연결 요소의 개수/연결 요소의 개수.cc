/*
    3초 제한
    1<=N<=1,000
    0<=M<=NC2

*/

/*
    DFS 초기 세팅
    - 그래프 배열 표현
    - 방문 배열 초기화
    - 스택에 시작 노드 넣기
*/

/*
    N(Node 개수), M(Edge 개수) -> int
    graph(그래프 데이터 저장 인접 리스트)   // 이차원 벡터 형태
    // 크기: 노드 수/ 0, 1, ... , N
    // 보통 그래프는 인접 리스트로 구현한다. 
        e.g.,
        {{4,5,7},
        {6,8,9},
        {1},
        ...
        }
    visited(방문 기록 저장 배열)

    graph 크기 N+1 재설정
    visited 크기 N+1, false 초기화


    for (M의 개수만큼 반복){
        graph에 그래프데이터 채우기
    }
    for (N의 개수만큼 반복){
        if (방문한 노드가 없으면){
            연결 요소 count ++
            DFS 실행
        }
    }

    DFS{    // DFS 구현
        if(현재 노드 == 방문 노드) return;
        visited 배열에 현재 노드 방문 기록
        for(현재 노드에서 연결된 모든 노드 탐색){
            if(현재 노드의 연결 노드 중 방문하지 않은 노드){
                DFS 실행(방문하지 않은 노드)
            }
        }
    
    }

*/

#include <iostream>
#include <vector>
using namespace std;

static vector<vector<int>> graph;
static vector<bool> visited;
void DFS(int start_node);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, M; 
    cin >> N >> M;
    graph.resize(N+1);
    visited = vector<bool>(N+1, false);
    int count=0;

    for (int i=0; i<M; ++i){
        int node1, node2;
        cin >> node1 >> node2;
        graph[node1].push_back(node2);
        graph[node2].push_back(node1);
    }
    for (int i=1; i<=N; ++i){
        if (!visited[i]){
            count++;
            DFS(i);
        }
    }

    cout << count;
    return 0;
}

void DFS(int start_node){
    if (visited[start_node]) return;
    visited[start_node] = true;
    // for (int i=0; i<graph[start_node].size(); ++i)
    for (int i: graph[start_node]){
        if (!visited[i]){
            DFS(i);
        }
    }
}