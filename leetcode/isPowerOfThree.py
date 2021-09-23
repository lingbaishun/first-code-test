class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = False
        if n == 1:
            return True
        else:
            n = n/3
            if n == 0:
                return False
            if str(n).replace('.0', '').isdigit():
                n = int(n)
                result = self.isPowerOfThree(n)
            else:
                return False
        return result

Solution_num = Solution()
print(Solution_num.isPowerOfThree(45))