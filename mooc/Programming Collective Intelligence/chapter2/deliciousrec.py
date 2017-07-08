from pydelicious import get_popular,get_userposts,get_urlposts

def initializeUserDict(tag,count=5):
    user_dict={}
    # get the top count' popular posts
    for p1 in get_popular(tag=tag)[0:count]:
        # find all users who posted this
        for p2 in get_urlposts(p1['href']):
            user=p2['user']
            user_dict[user]={}
    return user_dict
from deliciousrec import *
delusers = initializeUserDict('programming')
delusers ['tsegaran'] = {} # 如果你也是用 delicious，则将自己也加入字典中
fillItems(delusers)