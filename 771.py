class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        list1 = list(J)
        list2 = list(S)
        num = 0
        for i in range(len(J)):
            Jewel = list1[i]
            for j in range(len(S)):
                if Jewel == list2[j]:
                    num += 1
        return num

    def numJewelsInStones(self, J, S):
        """
        :param J: str
        :param S: str
        :return: int
        """
        num = 0
        list1 = list(J)
        for i in range(len(list1)):
            if list1[i] in S:
                bonus = S.count(list1[i])
                num += bonus
        return num

    def numJewelsInStones(self, J, S):
        """
        beat 100%
        :param J: str
        :param S: str
        :return: int
        """
        num = 0
        list1 = list(J)
        for i in range(len(list1)):
            bonus = S.count(list1[i])
            num += bonus
        return num