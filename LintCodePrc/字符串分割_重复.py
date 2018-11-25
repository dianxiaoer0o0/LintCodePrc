# encoding:utf-8
class Solution:
    """
    @param s: the string s
    @param k: the maximum length of substring
    @return: return the least number of substring
    """

    def getAns(self, s, k):
        # Write your code here
        n = 0
        #L = len(s)
        i = 0
        while i < s.__len__():
            j = 1
            while j < k and i+j < s.__len__():
                if s[i + j] == s[i]:
                    j += 1
                else:
                    break

            print s[i:i+j]
            i += j
            n += 1
        return n
s = "bbbcabcab"
k = 2

a = Solution()
print a.getAns(s,k)