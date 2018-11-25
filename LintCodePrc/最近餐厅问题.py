#encoding:utf-8
import random
class Solution:
    """
    @param restaurant:
    @param n:
    @return: nothing
    """

    def nearestRestaurant(self, restaurant, n):
        # Write your code here
        if restaurant == [] or n == 0 or n > len(restaurant):
            return []
        dis = {}
        for each in restaurant:
            if tuple(each) not in dis:
                dis[tuple(each)] = pow(each[0], 2) + pow(each[1], 2)
            else:
                dis[(each[0] + 1000, each[1] + 1000)] = pow(each[0], 2) + pow(each[1], 2)
        sortedDis = sorted(dis.items(), key=lambda item: item[1])
        maxDis = sortedDis[n - 1][1]
        i = 1
        answer = []
        for each in restaurant:

            if dis[tuple(each)] <= maxDis:
                answer.append(each)
                i += 1
            if i == n + 1:
                return answer


a = Solution()
#restaurants = [[[111,11],[121,222],[133,321],[111,224],[121,325],[121,12],[113,213],[124,124],[311,125],[132,245],[232,213],[122,324],[132,514],[113,321],[323,114],[323,512],[224,521],[532,125],[13,223],[33,14],[3,52],[24,35],[12,514],[132,333],[312,134],[311,521],[214,513],[532,125],[132,212],[3,14],[321,512],[421,135]],[[1,1],[1,2],[1,3],[1,4],[1,5],[2,2],[2,3],[2,4],[2,5],[3,3],[3,4],[3,5]],[[0,1],[1,2],[2,1],[1,0]]]
#ns = [30,7,3]
x=[]
restaurants = []
ns = []
for i in range(1000000):
    x.append([random.randint(1,1000),random.randint(1,1000)])
restaurants.append(x)
ns.append(100)
for i in range(len(restaurants)):
    print (a.nearestRestaurant(restaurants[i],ns[i]))