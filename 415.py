class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1)
        num2 = list(num2)
        suma = 0
        sumb = 0
        for numa in num1:
            suma = 10*suma + int(numa)
        for numb in num2:
            sumb = 10*sumb + int(numb)
        return suma+sumb
