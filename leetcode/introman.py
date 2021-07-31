

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str_out = ''
        num_M = int(num / 1000)
        str_out = str_out + 'M' * num_M
        num = num - num_M * 1000
        if int(num / 100) == 9:
            str_out = str_out + 'CM'
            num = num - 900
        if int(num / 100) == 4:
            str_out = str_out + 'CD'
            num = num - 400
        num_D = int(num / 500)
        str_out = str_out + 'D' * num_D
        num = num - num_D * 500
        num_C = int(num / 100)
        str_out = str_out + 'C' * num_C
        num = num - num_C * 100
        if int(num / 10) == 9:
            str_out = str_out + 'XC'
            num = num - 90
        if int(num / 10) == 4:
            str_out = str_out + 'XL'
            num = num - 40
        num_L = int(num / 50)
        str_out = str_out + 'L' * num_L
        num = num - num_L * 50
        num_X = int(num / 10)
        str_out = str_out + 'X' * num_X
        num = num - num_X * 10
        if num == 9:
            str_out = str_out + 'IX'
            num = num - 9
        if num == 4:
            str_out = str_out + 'IV'
            num = num - 4
        num_V = int(num / 5)
        str_out = str_out + 'V' * num_V
        num_I = num - num_V * 5
        str_out = str_out + 'I' * num_I
        return str_out


Solution_num = Solution()
print(Solution_num.intToRoman(58))