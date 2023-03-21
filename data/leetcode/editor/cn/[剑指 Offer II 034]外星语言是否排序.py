# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = dict()
        i = 1
        for c in order:
            dic.__setitem__(c, i)
            i += 1
        dic.__setitem__('', 0)

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(max(len(word1), len(word2))):
                if j >= len(word1):
                    break
                if j >= len(word2):
                    return False
                c1 = word1[j]
                c2 = word2[j]
                if dic.get(c1) > dic.get(c2):
                    return False
                elif dic.get(c1) < dic.get(c2):
                    break
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
# leetcode submit region end(Prohibit modification and deletion)
