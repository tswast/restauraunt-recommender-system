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
get_ipython().magic(u'save getalexratings.py 1-36')
pickle.dump(smallbizs, "smallbizs.pickle")
pickle.dump(smallbizs, open("smallbizs.pickle", "wb"))
pickle.dump(smallfriends, open("smallfriends.pickle", "wb"))
pickle.dump(x_done, open("x_done.pickle", "wb"))
pickle.dump(theta_done, open("theta_done.pickle", "wb"))
alex_t = theta_done[alex_i]
theta_doen.shape
theta_done.shape
alex_p = np.asmatrix(alex_t) * np.asmatrix(x_done.transpose())
alex_p
np.argmax(alex_p)
np.argsort(alex_p)
alex_biz_i = np.argsort(alex_p)
alex_biz_i[:-5]
alex_biz_i[-5:]
alex_biz_i[-3:]
alex_biz_i[,-3:]
alex_biz_i[:,-3:]
alex_biz_i[:,-5:]
np.asarray(alex_biz_i[:,-5:])
np.asarray(alex_biz_i[-5:])
np.asarray(alex_biz_i[:,-5:])
np.asarray(alex_biz_i[:,-5:]).ravel()
smallbizs[np.asarray(alex_biz_i[:,-5:]).ravel()]
alex_p[np.asarray(alex_biz_i[:,-5:]).ravel()]
alex_p[:,np.asarray(alex_biz_i[:,-5:]).ravel()]
alex_p[:,np.asarray(alex_biz_i[:,-10:]).ravel()]
smallbizs[np.asarray(alex_biz_i[:,-10:]).ravel()]