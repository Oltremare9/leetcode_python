# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                count = 0
                for pair in roads:
                    if i == pair[0] or i == pair[1] or j == pair[0] or j == pair[1]:
                        count += 1
                if count > res:
                    res = count
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximalNetworkRank(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]))
# leetcode submit region end(Prohibit modification and deletion)
