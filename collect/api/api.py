# facebook API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN="EAACEdEose0cBAD1ZA0bZBXMO2CG8WZCRWSLRpaAMBFzUyAuxrOYLQyDaWXPzvFrRa8yELZBPLD4laB7ZCZC4qJD32azw1GobysSjIZAFvowNrt1NSZCB58QnI1DMoSqeHjfGm1dnSYN7hVQRw2BvZAVT2BnjIUKw3UjaaUXjDnEI0u73Wm9aVla3ZCSBEE0rd527vhilPduOqiVgZDZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"     #고정된 값이고 주소 외우삼


def fb_gen_url(
        base=BASE_URL_FB_API,
        node='', #안넣을수도있으니까 기본값으로
        **params):      #페이스북 url을 generatic을 한다.
    url = '%s/%s/?%s' % (base, node, urlencode(params))
    return url
# return '%s/%s/posts/?%s' % (base,node, urlencode(params))
#     이 방법도 가능

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    return json_result.get("id")


def fb_fetch_posts(pagename, since, until):

    url = fb_gen_url(
        node=fb_name_to_id(pagename)+"/posts/",
        fields='id, message, link, name, type, shares, reactions, created_time, comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN)

    print(url)
    json_result = json_request(url=url)
    print(json_result)