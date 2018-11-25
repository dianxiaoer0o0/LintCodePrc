#encoding:utf-8


class Solution():

#动态规划思想
    def c(self,a,b):
        i = b
        up = a
        down  = b
        while i > 1 :
            up *= (a-i+1)
            down *= (b-i+1)
            i -= 1
        return up/down

    def iPossibilitys(self,i,n):
        if i<1 or i>6*n:
            return 0
        if n == 1:
            return 1
        else:
            return self.iPossibilitys(i-1,n-1)+self.iPossibilitys(i-2,n-1)+self.iPossibilitys(i-3,n-1)+self.iPossibilitys(i-4,n-1)+self.iPossibilitys(i-5,n-1)+self.iPossibilitys(i-6,n-1)

    def probability(self,i,n):
        allPossibilitys = pow(6,n)
        #total = [sum(y for y in x) for x in self.unName(n)]
        return float(self.iPossibilitys(i,n))/allPossibilitys

    def dicesSum(self, n):
        s = []
        for i in range(n,6*n+1):
            s.append([i,])
            s[i-n].append(self.probability(i,n))
        return s

    def addSingle(self,a,carry):
        a = a + carry
        if a>6:
            a = 1
            carry = 1
        else:
            carry = 0
        return a, carry

    def addCase(self,case):
        n = len(case)
        case[0],carry = self.addSingle(case[0],1)
        for i in range(1,n):
            case[i],carry = self.addSingle(case[i],carry)
        return case

    def unName(self,n):
        case = [1 for i in range(n)]
        case[0] = 0
        while case != [6 for i in range(n)]:
            case = self.addCase(case)
            yield case

a = Solution()
for x in a.unName(3):
    print x
print [sum(y for y in x) for x in a.unName(3)]
print a.iPossibilitys(12,2)
print a.dicesSum(7)

