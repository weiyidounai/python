# A dictionary of movie critics and their ratings of a small
# set of movies
#一个涉及影评者及其对几部影片评分情况的字典
from math import sqrt

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


# print(critics['Lisa Rose']['Lady in the Water'])
# print(critics['Toby']['Snakes on a Plane'])
# print(critics['Toby'])
# print(sqrt(pow(5-4,2)+pow(4-1,2)))
# print((1/(1+sqrt(pow(1,2)+pow(3,2)))))

# Returns a distance-based similarity score for person1 and person2
#返回一个有关person1和person2的基于距离的相似度评价
def sim_distance(prefs,person1,person2):
 # Get the list of shared_items
 si={}
 for item in prefs[person1]:
    if item in prefs[person2]:
        si[item]=1

    # if they have no ratings in common, return 0
    if len(si)==0: return 0

    # Add up the squares of all the differences计算所有差值的平方和
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)
#
# print('similar')
# print(sim_distance(critics,'Lisa Rose','Gene Seymour'))
# print("\n")

# Returns the Pearson correlation coefficient for p1 and p2
#返回p1和p2的皮尔逊相关系数
def sim_pearson(prefs,p1,p2):
 # Get the list of mutually rated items得到双方都曾评价过的物品列表
 si={}
 for item in prefs[p1]:
    if item in prefs[p2]:
        si[item]=1
 # Find the number of elements得到列元素的个数
 n=  len(si)
 # if they are no ratings in common, return 0如果两者没有共同之处
 if n == 0:
     return 0
 # Add up all the preferences对所有偏好求和
 sum1 = sum([prefs[p1][it] for it in si])
 sum2 = sum([prefs[p2][it] for it in si])
 # Sum up the squares求平方和
 sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
 sum2Sq = sum([pow(prefs[p2][it],2) for it in si])
 # Sum up the products求乘积之和
 pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])
 # Calculate Pearson score计算皮尔逊评价值
 num = pSum-(sum1*sum2/n)
 den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
 if den == 0: return 0
 r = num/den
 return r

#print(sim_pearson(critics,'Lisa Rose','Gene Seymour'))

#为评论者打分
# Returns the best matches for person from the prefs dictionary.
#从反应偏好的字典中返回最佳匹配者
# Number of results and similarity function are optional params.
#返回结果的个数和相似度函数均为可选参数
def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs, person, other),other)
        for other in prefs if other!= person]
# Sort the list so the highest scores appear at the top
    #对列表进行排序，评价值最高者排在最前面
    scores.sort()
    scores.reverse()
    return scores[0:n]
print('为Toby返回相似度最大的三个推荐：\n', topMatches(critics,'Toby',n=3))

# Gets recommendations for a person by using a weighted average
#利用所有他人评价值的加权平均，为某人提供建议
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
    # don't compare me to myself不与自己比较
        if other == person: continue
        sim = similarity(prefs,person,other)
        # ignore scores of zero or lower忽略瓶价值为0或者<0
        if sim <= 0 :  continue
        for item in prefs[other]:
            # only score movies I haven't seen yet只对自己为看的影片评价
            if item not in prefs[person] or prefs[person][item]==0:
                # Similarity * Score
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                # Sum of similarities
                simSums.setdefault(item,0)
                simSums[item]+=sim
    # Create the normalized list建立一个归一化的列表
    rankings = [(total/simSums[item],item) for item,total in totals.items()]
    # Return the sorted list返回经过排序的列表
    rankings.sort()
    rankings.reverse()
    return rankings
print('计算加权为Toby提供推荐\n', getRecommendations(critics,'Toby'))
# print(getRecommendations(critics,'Toby',
#                          ... similarity=sim_distence))

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, { })
            # Flip item and person物品与人员对调
            result[item][person]=prefs[person][item]
    return result
movies = transformPrefs(critics)
print('与Superman Returns相似度的高的商品\n', topMatches(movies, 'Superman Returns'))
print('根据物品相似度找到与自己相似的人\n', getRecommendations(movies, 'Just My Luck'))

def calculateSimilarItems(prefs,n=10):
    # Create a dictionary of items showing which other items they
    #建立字典，以给出与这些物品最为详尽的所有其他物品
    # are most similar to.
    result={}
    # Invert the preference matrix to be item-centric以物品为中心对偏好矩阵实施倒置处理
    itemPrefs=transformPrefs(prefs)
    c=0
    for item in itemPrefs:
    # Status updates for large datasets针对大数据集更新状态变量
        c+=1
        if c%100==0: print ("%d / %d" % (c,len(itemPrefs)))
        #Find the most similar items to this one寻找最相近的物品
        scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
        result[item]=scores
    return result
print("物品相似度的数据集：\n", calculateSimilarItems(critics))


