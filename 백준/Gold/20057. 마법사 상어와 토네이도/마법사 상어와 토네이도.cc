#include <iostream>
#include <cmath>
using namespace std;
int N, sand = 0; // 격자 크기, 모래의 양
int cDir = 0; // 좌측 방향부터 시작
int num = 1; // 현재 이동 크기
int A[500][500] = { 0, }; // 격자
int cR, cC; // 현재 위치
int dir[4][2] = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}}; // 좌하우상 : 토네이도 이동 순서
int diff[4][9][3] = {{ // 확산 방향과 비율: {r, c, %}
        // 좌
        {-1, 1, 1}, {1, 1, 1}, {-2, 0, 2}, 
        {2, 0, 2}, {0, -2, 5}, {-1, 0, 7}, 
        {1, 0, 7}, {-1, -1, 10}, {1, -1, 10}
    }, {
        // 하
        {-1, -1, 1}, {-1, 1, 1}, {0, -2, 2}, 
        {0, 2, 2}, {2, 0, 5}, {0, -1, 7}, 
        {0, 1, 7}, {1, -1, 10}, {1, 1, 10}
    }, {
        // 우
        {-1, -1, 1}, {1, -1, 1}, {-2, 0, 2}, 
        {2, 0, 2}, {0, 2, 5}, {-1, 0, 7}, 
        {1, 0, 7}, {-1, 1, 10}, {1, 1, 10}
    }, {
        // 상
        {1, -1, 1}, {1, 1, 1}, {0, -2, 2}, 
        {0, 2, 2}, {-2, 0, 5}, {0, -1, 7}, 
        {0, 1, 7}, {-1, -1, 10}, {-1, 1, 10}
    }
};

void move() {
    cR += dir[cDir][0]; cC += dir[cDir][1]; // 위치 y로 이동
    int remain = A[cR][cC]; // 남은 모래 양, 일단 현재 위치 y의 값을 저장
    for (int i = 0; i < 9; ++i) {
        // 비율이 새겨진 다음 위치들
        int nR = cR + diff[cDir][i][0];
        int nC = cC + diff[cDir][i][1];
        int value = trunc(A[cR][cC] * diff[cDir][i][2] / 100); // 현재 위치 값 기준 해당 비율만큼의 모래 (소숫점 아래 버림)
        if (nR < 0 || nR >= N || nC < 0 || nC >= N) sand += value; // 격자 밖으로 나간 모래
        else A[nR][nC] += value; // 각 위치 값 갱신
        remain -= value; // 모래 비율만큼의 값을 빼줌
    }
    int aR = cR + dir[cDir][0], aC = cC + dir[cDir][1]; // 위치 α 좌표
    if (aR < 0 || aR >= N || aC < 0 || aC >= N) sand += remain; // 위치 α도 격자 밖으로 나간 경우, 남은 값 모두 밖으로 빼내기
    else A[aR][aC] += remain; // 남은 모래를 위치 α에 더해주기
    A[cR][cC] = 0; // y에 있던 모래 모두 α로 이동되었으므로 0
}

void tornado() {
    cR = cC = N / 2; // 현재 위치 (정가운데)
    while (num < N) { // 이동 크기 num이 N보다 작을 때까지만 이동
        for (int i = 0; i < 2; ++i) { // 이동 크기 2번씩 반복
            for (int j = 0; j < num; ++j) move(); // 한 칸씩 총 num만큼 이동
            cDir = (cDir + 1) % 4; // 이동 방향 변경
        }
        num++; // 이동 크기 1 증가
    }
    // 마지막 최상단 줄 N - 1만큼 이동
    for (int j = 0; j < num - 1; ++j) move(); // 한 칸씩 총 num만큼 이동
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    cin >> N;
    for (int r = 0; r < N; ++r)
        for (int c = 0; c < N; ++c)
            cin >> A[r][c];
    tornado();
    cout << sand;
    return 0;
}