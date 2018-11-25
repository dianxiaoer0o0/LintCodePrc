class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        # write your code here
        if B == "":
            return True
        elif A == "":
            return False
        strA = list(A)
        for char in B:
            if char not in strA:
                return False
        return True