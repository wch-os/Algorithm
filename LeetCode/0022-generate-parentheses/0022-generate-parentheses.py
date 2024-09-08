class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def solve(cnt1, cnt2, arr, result):
            if len(arr) == n * 2 and cnt1 == n and cnt2 == n:
                result.append("".join(arr))
                return

            # ')'의 수가 '(' 보다 많으면 안 됨
            if cnt1 < cnt2 or cnt1 > n:
                return

            arr.append("(")
            solve(cnt1 + 1, cnt2, arr, result)
            arr.pop()

            arr.append(")")
            solve(cnt1, cnt2 + 1, arr, result)
            arr.pop()

        arr = []  # 괄호 배열
        result = []  # 올바르게 구성된 괄호의 모든 조합 배열
        solve(0, 0, arr, result)
        return result
