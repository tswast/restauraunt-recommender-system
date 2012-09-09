import numpy as np
_ip.magic(r"cd C:\Users\tswast\Dropbox\Projects\RestaurantRecommender")
from glob import glob
for friendpath in glob("reviews/*.json"):
friends = {}
for friendpath in glob("reviews/*.json"):
    import json
    friends[friendpath] = json.load(open(friendpath))
    

friends
fids = [key for key in friends.keys()]
fids
biz_set = set()
for f in fids:
    biz_set.add(friends[f].keys())
    

for f in fids:
    biz_set.update(friends[f].keys())
    

biz_set
bizs = list(biz_set)
bizs
fids
len(fids)
len(bizs)
from __future__ import division
len(bizs) / len(fids)
sum([len(friends[f]) for f in fids])
sum([len(friends[f]) for f in fids]) / len(fids)
ratings = np.zeros((len(bizs), len(fids)))
ratings.shape
for f in fids:
bizi = {}
for biz in bizs:
for i, biz in enumerate(bizs):
    bizi[biz] = i
    

for f in fids:
for fi, f in enumerate(fids):
    for b in friends[f]:
        bi = bizi[b]
        r = friends[f][b]
        ratings[bi,fi] = r
        

ratings
ratings.sum()
ratings.sum(axis=0)
Y = ratings
R = ratings > 0
R
json.dump({"Y":Y, "R":R, "friends":fids, "bizs":bizs}, "ratings.pickle")
import pickle
pickle.dump({"Y":Y, "R":R, "friends":fids, "bizs":bizs}, open("ratings.pickle", "w"), -1)
p_ratings = pickle.load(open('ratings.pickle'))
pickle.dump({"Y":Y, "R":R, "friends":fids, "bizs":bizs}, open("ratings.pickle", "wb"), -1)
p_ratings = pickle.load(open('ratings.pickle'))
p_ratings = pickle.load(open('ratings.pickle', "rb"))
p_ratings
p_ratings.Y
p_ratings["Y"]
_ip.magic("save buildmatrix.py 1-47")
