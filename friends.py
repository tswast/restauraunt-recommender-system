# coding: utf-8
import lxml.html
html = lxml.html.parse(http://www.yelp.com/user_details_friends?userid=hX5D5lXijHFcm4WGtaRKng)
html = lxml.html.parse("http://www.yelp.com/user_details_friends?userid=hX5D5lXijHFcm4WGtaRKng")
frienddivs = html.cssselect("div.user-passport")
import urllib
f_html = urllib.open("http://www.yelp.com/user_details_friends?userid=hX5D5lXijHFcm4WGtaRKng")
f_html = urllib.urlopen("http://www.yelp.com/user_details_friends?userid=hX5D5lXijHFcm4WGtaRKng")
html_str = "".join(f_html.readlines())
f_html.close()
doc = lxml.html.fromstring(html_str)
frienddivs = doc.cssselect("div.user-passport")
len(frienddivs)
friendids = []
for frienddiv in frienddivs:
    friendids.append(frienddiv.cssselect("div.photoBox a")[0].get("href"))
    
friendids
friendids_p = []
for id in friendids:
    import re
    friendids_p.append(re.sub(".+=", "", id))
    
friendids_p
import json
f = open("friends.json", "w")
json.dump(friendids_p, f)
f.close()