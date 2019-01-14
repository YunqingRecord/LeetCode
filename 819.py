import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        cur = 0
        ans = 0
        fin = ''
        paragraph = paragraph.lower()
        pro = re.split(r"[;,!?`~.\s']", paragraph)
        for p in pro:
            if p not in banned:
                if p != '':
                    cur = pro.count(p)
            if ans < cur:
                ans = cur
                fin = p
        return fin
