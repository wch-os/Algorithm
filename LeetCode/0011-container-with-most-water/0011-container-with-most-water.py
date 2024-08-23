# 풀이 시간: 7분
# 시간복잡도: O(n)
# 공간복잡도: O(n)
# 유형: two pointer, greedy
# 참고: -

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        e = len(height) - 1

        result = 0

        while s < e:
            result = max(result, (e - s) * min(height[s], height[e]))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1

        return result