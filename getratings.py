from .myurllib import urlopen
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

