#encoding:utf-8
class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        # write your code here
        strInOrder = ["".join(sorted(list(x))) for x in strs]
        i = 0
        anagram = []
        while strInOrder != []:
            str = strInOrder.pop(0)
            originalStr = strs.pop(0)
            if str in strInOrder:
                anagram.append(originalStr)
                while 1:
                    if str in strInOrder:
                        j = strInOrder.index(str)
                        anagram.append(strs.pop(j))
                        del strInOrder[j]
                    else:
                        break

        # dic = {}
        # anagrams = []
        # for str in strInOrder:
        #     dic[str] = dic.get(str, 0) + 1;
        #     if dic[str] == 2:
        #         i = 0
        #         while i < len(strs):
        #             if strInOrder[i] == str:
        #                 anagrams.append(strs[i])
        #             i += 1

        return anagram


a = Solution()
strs = ["",""]
print(a.anagrams(strs))