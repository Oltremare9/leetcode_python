# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """

        sort_nums = sorted(nums, reverse=True)
        sum = 0
        for num in sort_nums:
            sum += num

        res = list()
        for query in queries:
            if sum <= query:
                res.append(len(nums))
            else:
                temp_sum = sum
                flag = False
                for i in range(len(sort_nums)):
                    temp_sum -= sort_nums[i]
                    if temp_sum <= query:
                        res.append(len(sort_nums) - i - 1)
                        flag = True
                        break
                if not flag:
                    res.append(0)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.answerQueries([1000000], [1000000]))

# leetcode submit region end(Prohibit modification and deletion)
