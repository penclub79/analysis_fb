# facebook API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN="EAACEdEose0cBADgOdTJTSycpfyS8DitIwD3mimFTbu53nwBUNNc37YYYiFxaZAXJ5zuKHEmHZBUezVjyTv8jB8bBhmS71KK4mzoZAN0mZAcSKJvOqDC2a4VYAnyMcPF5cXMctfDIUvd89ZAoZAM88PkWULZAafe5pa76PBWsZCSfshNAc56beWgrUhNwof9ThcZAxmgHnnOZCaZBwZDZD"
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
    # json_result = json_request(url=url)
    # print(json_result)
    #리스트로 N개를 받기위한 함수

    # results = []
    isnext = True   #true냐 false에 따라서 달라고하기
    while isnext is True: # isnext가 true면 루프돌기
        json_result = json_request(url=url)
        #페이징 정보 가져오기 왜? json result가 null일수 있어서
        paging = None
        if json_result is None:
            paging =  None
        else:
            paging = json_result.get('paging') #none이 아니면 paging을 가져오자
    #위 코드는 단순 코드임
    #삼항연산자 쓰면 더 간결함
    # isnext = True
    # while isnext is True:
    #     json_result = json_request(url=url)
    #     paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        # results += posts #posts의 새로운 50개 리스트를 추가 하는 과정 append는 업데이트됨 ㅎㅎ
        url = None if paging is None else paging.get("next") #마지막 posts의 경우 null로 나타남
        #roop돌때 url을 다시 쓰려고 url로 잡아줌
        isnext = url is not None

    # return results  #roop가 끝난다음에 결과를 출력하기 위해 바깥에 씀
        yield posts  #얘는 for문 안에 넣어야 된다