# coding: utf-8
import urllib
f = urllib.urlopen("http://www.yelp.com/user_details_reviews_self?userid=hX5D5lXijHFcm4WGtaRKng")
lines = f.readlines()
lines
f.close()
f = urllib.urlopen("http://www.yelp.com/user_details_reviews_self?userid=hX5D5lXijHFcm4WGtaRKng&rec_pagestart=10")
f.close()
for page_i in range(26):
    f = urllib.urlopen("http://www.yelp.com/user_details_reviews_self?userid=hX5D5lXijHFcm4WGtaRKng&rec_pagestart={}".format(page_i * 10))
    with open("alex.{:01d}.html".format(page_i), "w") as g:
        g.write("".join(f.readlines())
    f.close()
    
for page_i in range(26):
    f = urllib.urlopen("http://www.yelp.com/user_details_reviews_self?userid=hX5D5lXijHFcm4WGtaRKng&rec_pagestart={}".format(page_i * 10))
    with open("alex.{:01d}.html".format(page_i), "w") as g:
        g.write("".join(f.readlines()))
    f.close()
    