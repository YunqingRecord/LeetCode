class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ok = num//10
        while num > 10:
            num += ok+(num-10*ok)
        return num

    def addDigits1(self,num):
        '''
        :param num: int
        :return: int
        '''
        num = (num - 1)%9 +1
        return num