# coding: utf-8
get_ipython().magic(u'save extractrating.0.py 1-34')
f.close()
htmls = []
for index in range(26):
    htmls.append(lxml.html.fromstring("".join(f.
   htmls.append(lxml.html.fromstring("".join(f.
   
   
   
   ))
   
for index in range(26):
    with open("alex.{}.html".format(index)) as f:
        htmls.append(lxml.html.fromstring("".join(f.readlines()))
        
        
    
        )
        
htmls
ratings = {}
for index in range(26):
    for review in htmls[index].cssselect("div.review"):
        biz = review.cssselect("div.biz_info h4 a")[0].get("href")
        biz = re.sub(r"#.*", "", biz)
        
for index in range(26):
    for review in htmls[index].cssselect("div.review"):
        biz = review.cssselect("div.biz_info h4 a")[0].get("href")
        biz = re.sub(r"#.*", "", biz)
        rating_str = review.cssselect("div.rating img")[0].get("alt")
        rating = float(rating_str.split()[0])
        ratings[biz] = rating
        
ratings
import json
json.dump(ratings, "alex.json")
json.dump(ratings, open("alex.json", "w"))
json.dump(ratings, open("alex.json", "w"), indent=True)