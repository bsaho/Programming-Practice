class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n==3:
            return 2
        else:
            nMinus= n/3
            if (n % 3)== 0:
                return 3 ** nMinus
            elif (n % 3) == 1:
                return (2 * 2  * (3 ** (nMinus-1)))
            else:
                return 2 * (3 ** nMinus)
            
            
        