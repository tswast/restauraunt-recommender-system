# coding: utf-8
xsave = pickle.load(open("xsave.v2.pickle", "rb"))
import pickle
xsave = pickle.load(open("xsave.v2.pickle", "rb"))
x0 = np.random.normal(size=10 * sum(ratings["R"].shape))
import numpy as np
ratings = pickle.load(open("ratings.pickle"))
smally = pickle.load(open("smally.pickle", "rb"))
smallr = smally > 0
smally.shape
x_done = xsave[:24200]
x_done
x_done.reshape((2420, 10))
x_done
x_done = x_done.reshape((2420, 10))
theta_done = xsave[24200:]
theta_done.reshape((81, 10))
theta_done = theta_done.reshape((81, 10))
ratings
ratings.keys()
smallbizs = ratings["bizs"]
smallfriends = ratings["friends"]
y = ratings["Y"]
y.shape
r = y > 0
r.sum(axis=1).shape
r.sum(axis=1)
smallbizs = smallbizs[r.sum(axis=1) > 1]
smallbizs = smallbizs.shape
smallbizs = np.array(smallbizs)[r.sum(axis=1) > 1]
smallbizs.shape
theta_done.shape
smallfriends = np.array(smallfriends)[r.sum(axis=0) > 1]
smallfriends.shape
smallfriends
for i, f in enumerate(smallfriends):
    if f.startswith("reviews\\hX"):
        print i, f
        
alex_i = 37