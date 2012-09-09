# coding: utf-8
import pickle
import scipy.optimize
import numpy as np
xsave = None
xsave = pickle.load(open("xsave.pickle", "rb"))
xsave
import numpy.random
def printprogress(xk):
    xsave = xk
    if numpy.random.randint(20) == 0:
        print "Cost:", costfunc.cost(xsave, smallr, smally)
        
def printprogress(xk):
    global xsave
    if numpy.random.randint(20) == 0:
        print "Cost:", costfunc.cost(xsave, smallr, smally)
        xsave = xk
        
import costfunc
smally = pickle.load(open("smally.pickle", "rb"))
smallr = smally > 0
xout = scipy.optimize(costfunc.cost, xsave, costfunc.cost_grad, (smallr, smally), callback=printprogress)
xout = scipy.optimize.fmin_cg(costfunc.cost, xsave, costfunc.cost_grad, (smallr, smally), callback=printprogress)
xout = scipy.optimize.fmin_cg(costfunc.cost, xsave, costfunc.cost_grad, (smallr, smally), callback=printprogress)
pickle.dump(open("xsave.v2.pickle", "wb"))
pickle.dump(xsave open("xsave.v2.pickle", "wb"))
pickle.dump(xsave, open("xsave.v2.pickle", "wb"))
get_ipython().magic(u'save progress.py 1-19')