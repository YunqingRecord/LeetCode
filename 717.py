
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        pt = 0
        le = len(bits)
        if le == 1:
            if bits[0] == 0:
                return True
            else:
                return False
        if le == 2:
            if bits[0] == 1:
                return False
            else:
                return True
        if le >= 3:
            for i in range(le):
                if pt <= le - 3:
                    if bits[pt] == 1:
                        pt += 2
                        if pt == le-1:
                            return True
                    elif bits[pt] == 0:
                        pt += 1
                    if pt == le-2:  # bits[le-1] == 0 definitely
                        if bits[pt] == 1:
                                return False
                        elif bits[pt] == 0:
                            return True
                        else:
                                return False


