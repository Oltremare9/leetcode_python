# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i in range(len(nums)):
            dic.__setitem__(nums[i], i)
        for i in range(len(nums)):
            if dic.__contains__(target - nums[i]) and i != dic.get(target - nums[i]):
                return [i, dic.get(target - nums[i])]
        return [0, 1]


if __name__ == "__main__":
    solution = Solution()
    sum = solution.twoSum(nums=[3, 2, 4], target=6)
    print(sum)
# leetcode submit region end(Prohibit modification and deletion)
