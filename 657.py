class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dic = {'U':1,'D':-1,'R':-0.5,'L':0.5}
        sum = 0
        for move in moves:
            sum += dic[move]
        return not bool(sum)