# coding: utf-8
import lxml.html
from .urllib import urlopen
def getratings(id):
        has_more = True
        page = 0
        ratings = {}
        while has_more:
                f = urlopen("http://www.yelp.com/user_details_reviews_self?userid={id}&rec_pagestart={}".format(page * 10, id=id))
                doc = lxml.html.fromstring("".join(f.readlines()))
                f.close()
                has_more = len(doc.cssselect("#pager_page_next")) != 0
                for review in doc.cssselect("div.review"):
                        biz = review.cssselect("div.biz_info h4 a")[0].get("href")
                        biz = re.sub(r"#.*", "", biz)
                        rating_str = review.cssselect("div.rating img")[0].get("alt")
                        rating = float(rating_str.split()[0])
                        ratings[biz] = rating
                    page = page + 1
                return ratings
        
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
import myurllib
from myurllib import urlopen
from .myurllib import urlopen
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
r = getratings(friendids_p[0])
import json
ids = json.load(open("friends.json"))
ids
r = getratings(ids[0])
import re
r = getratings(ids[0])
r
ids[0]
json.dump(r, open("{}.json".format(ids[0]), "w")
)
ids[0]
ids[0:1]
ids[1:2]
for id in ids[1:]:
    r = getratings(id)
    json.dump(r, open("{}.json".format(id), "w"))
    