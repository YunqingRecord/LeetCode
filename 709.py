class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        dic = {'A': 'a', "B": "b", "C": 'c', "D": 'd', 'E': 'e', "F": 'f', "G": 'g',
               "H": 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
               'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w',
               'X': 'x', 'Y': 'y', "Z": 'z'}
        list1 = list(str)
        str2 = ''
        for i in range(len(list1)):
            try:
                str2 += dic[list1[i]]
            except:
                str2 += list1[i]
        return str2


