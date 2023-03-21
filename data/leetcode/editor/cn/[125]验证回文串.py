# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        result = ''
        for c in s:
            if ('a' <= c <= 'z') or ('0' <= c <= '9'):
                result += c

        if result == '':
            return True
        for i in range(len(result)):
            if result[i] != result[len(result) - 1 - i]:
                return False

        return True
        # leetcode submit region end(Prohibit modification and deletion)
