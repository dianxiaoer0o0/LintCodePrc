#encoding:utf-8
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        lenS = len(source)
        lenT = len(target)
        if lenT == 0:
            return 0
        bingo = False
        for i in range(lenS):
            #x = source[i:i+lenT]
            if source[i:i+lenT] == target:
                bingo = True
                break
        if True:
            return i
        else:
            return -1

