/*
    제한 시간 2초 
    N<=1000, M<=1000
    최대 O^2
*/

/*
    N(노드 개수), M(edge 개수), V(탐색 시작하는 노드 번호)
    graph(인접 노드 리스트 벡터)
        // 두 노드 사이에 여러개 간선이 있을 수 있음
        // 간선은 양방향
    visited(방문 배열)
    trajectory(경로 배열)   // 전역 변수로 해야함

    cin N, M, V 결정
    graph 크기 결정
    visited 크기 결정, 초기화
    for (M만큼 반복){
        그래프에 인접 노드 채우기
    }
    
    // DFS 하는 단계
    DFS(V);     // 시작 노드에서 탐색 시작
    void DFS(node){
        node를 visited 에 반영
        node를 trajectory 에 추가
        for (node의 이웃만큼 반복){
            if (이웃을 visited하지 않았으면){
            DFS(이웃);
            }
        }
    }
    trajectory 출력

    // BFS 하는 단계
    visited 초기화
    trajectory 초기화
    myqueue(탐색해야하는 노드 목록)

    BFS(V);     // 시작 노드에서 탐색 시작
    void BFS(node){
        myqueue에 시작 노드 V 집어넣음
        while (myqueue가 빌 때까지 반복){
            queue에 있는 걸 pop.
            꺼낸 걸 visited에 반영
            꺼낸 걸 trajectory에 추가
            for (꺼낸 것의 이웃만큼 반복){
                if (visited 하지 않았으면)
                    이웃을 myqueue에 push
            }
        }
    }
    trajectory 출력
}
*/

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

static vector<vector<int>> graph;
static vector<bool> visited;
static vector<int> trajectory;
static queue<int> myQueue;

void DFS(int start_node);
void BFS(int start_node);

int main(){
    int nodeNo, edgeNo, start_node;
    cin >> nodeNo >> edgeNo >> start_node;
    graph.resize(nodeNo+1);
    visited = vector<bool>(nodeNo+1, false);
    
    
    for (int i=0; i<edgeNo; ++i){
        //그래프에 인접노드 채우기
        int node1, node2;
        cin >> node1 >> node2;
        graph[node1].push_back(node2);
        graph[node2].push_back(node1);
    }
    for (int i=1; i<=nodeNo; ++i){
        sort(graph[i].begin(), graph[i].end());
    }

    //DFS 하는 단계
    DFS(start_node);
    // cout << "DFS start" << "\n";
    for (int node:trajectory){
        cout << node << " ";
    }
    cout << "\n";

    //visited, trajectory 초기화
    // visited = vector<bool>(nodeNo+1, false);
    fill(visited.begin(), visited.end(), false);
    trajectory.clear();

    //BFS 하는 단계
    BFS(start_node);
    // cout << "BFS start" << "\n";
    for (int node:trajectory){
        cout << node << " ";
    }

    return 0;
}
void DFS(int start_node){
    trajectory.push_back(start_node);
    visited[start_node] = true;
    for (int neighbor: graph[start_node]){
        if (!visited[neighbor]){
            DFS(neighbor);
        }
    }
}
void BFS(int start_node){
    myQueue.push(start_node);
    visited[start_node] = true;
    
    while (!myQueue.empty()){
        int cur_node = myQueue.front();
        trajectory.push_back(cur_node);
        myQueue.pop();
        for (int neighbor: graph[cur_node]){
            if (!visited[neighbor]) {
                myQueue.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }
}