class Solution:
    def uniqueMorseRepresentations(self,words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.",
               'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.",
               'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-",
               'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."}
        trans = []
        length = len(words)
        for i in range(length):
            str_mid = ''
            form = list(words[i])
            for j in range(len(form)):
                str_mid += dic[form[j]]
            trans.append(str_mid)
        set1 = set(trans)
        lenn = len(set1)
        return lenn

    def uniqueMorseRepresentations(self,words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
               ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # ord('a') = 97
        trans = []
        length = len(words)
        for i in range(length):
            str_mid = ''
            form = list(words[i])
            for j in form:
                str_mid += dic[ord(j)-97]
            trans.append(str_mid)
        return len(set(trans))


