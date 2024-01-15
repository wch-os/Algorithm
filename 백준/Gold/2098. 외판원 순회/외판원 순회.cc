// 정답 코드
// https://velog.io/@jxlhe46/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-%EB%AC%B8%EC%A0%9C

#include <iostream>
#define INF 1e9 
using namespace std; 

int N, END;
int cost[16][16];
int dp[16][1 << 16]; 

int TSP(int now, int visited){
	// 모든 노드를 방문했는데 
	if(visited == END){
		// 현재 노드에서 0번으로 가는 경로가 있으면 
		if(cost[now][0] > 0){ 
			return cost[now][0]; // 최소 비용 반환 
		}

		return INF; // 불가능한 경우에는 INF 반환 
	}

	// 현재 상태를 이미 계산한 값이 dp 테이블에 있다면 그대로 사용
	if(dp[now][visited] != 0) return dp[now][visited];

	// 없으면 현재 노드에 대한 탐색 진행 
	dp[now][visited] = INF; 
    
	for(int i = 0; i < N; i++){
		// 현재 노드에서 i번 노드로 가는 경로가 없으면 패스
		if(cost[now][i] == 0) continue;
        
		// 이미 방문한 노드면 패스 
		if(visited & (1 << i)) continue;

		// i번 노드 방문 처리 후 최소 비용 반환 
		int temp = TSP(i, visited | 1 << i); 
		dp[now][visited] = min(dp[now][visited], cost[now][i] + temp); 
	}

	return dp[now][visited]; // 최소 비용 반환 
}

int main()
{ 
	ios::sync_with_stdio(0);
    cin.tie(0);

	cin >> N;
	END = (1 << N) - 1;

	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			cin >> cost[i][j]; 
		}
	}
	
	// 0번 노드부터 그래프 탐색 
	cout << TSP(0, 1) << "\n"; 

	return 0;
}