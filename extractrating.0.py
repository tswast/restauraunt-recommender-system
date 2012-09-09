# coding: utf-8
import lxml
get_ipython().magic(u'pwd ')
f = open("alex.0.html")
import lxml.html
html = lxml.html.parse(f)
html
html.tostring()
lxml.html.tostring(html)
help(lxml.html.find_class)
lxml.html.find_class(html, "biz_info")
html = lxml.html.fromstring("".join(f.readlines()))
html = lxml.html.fromstring("".join(f.readlines()))
f.close()
f = open("alex.0.html")
html = lxml.html.fromstring("".join(f.readlines()))
html.find_class("biz_info")
[elem.text_content() for elem in html.find_class("biz_info")]
[elem.cssselect("a").text_content() for elem in html.find_class("biz_info")]
[elem.cssselect("a")[0].text_content() for elem in html.find_class("biz_info")]
html.cssselect("div.review div.rating_info img")
[elem.get(alt) for elem in html.cssselect("div.review div.rating_info img")]
[elem.get("alt") for elem in html.cssselect("div.review div.rating_info img")]
reviews = html.cssselect("div.review")
reviews
reviews[0].cssselect("img")
reviews[0].cssselect("div.biz_info a")
reviews[0].cssselect("div.biz_info h4 a")
reviews[0].cssselect("div.biz_info h4 a")[0].get("href")
reviews[0].cssselect("div.rating img")[0].get("alt")
ratings = {}
for review in reviews:
    biz = review.cssselect(div.biz_info h4 a")[0].get("href")
    biz
    import re
    biz = re.sub(r"#.*", "", biz)
    print biz
    
for review in reviews:
    biz = review.cssselect("div.biz_info h4 a")[0].get("href")
    biz
    import re
    biz = re.sub(r"#.*", "", biz)
    print biz
    
for review in reviews:
    biz = review.cssselect("div.biz_info h4 a")[0].get("href")
    biz = re.sub(r"#.*", "", biz)
    rating_str = review.cssselect("div.rating img")[0].get("alt")
    rating = float(rating_str.split()[0])
    ratings[biz] = rating
    
ratings