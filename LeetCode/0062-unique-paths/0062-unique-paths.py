# 풀이 시간: 10분+ 15분
# 시간복잡도: O(m * n)
# 공간복잡도: O(m * n)
# 유형: dp
# 참고: -

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        board = [[0] * n for _ in range(m)]

        for i in range(m): # 행 1 초기화
            board[i][0] = 1

        for i in range(n): # 열 1 초기화
            board[0][i] = 1

        # board[i][j] = board[i-1][j] + board[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i-1][j] + board[i][j-1]

        return board[m-1][n-1]