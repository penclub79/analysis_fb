from datetime import datetime, timedelta #시간대 변경
                #datetime 패키지고 timedelta는 함수다.
from .api import api
import os
import json

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_post(post):      #data 전처리 적재하기전의 과정
    #공유수 변경 : 'share' 밑에 'count'를 바꾼단다.
    if 'shares' not in post:
        post['count_shares'] = 0
    else:
        post['count_shares'] = post['shares']['count']
        #바깥에서 편하게 쓰라고 전처리해줌

    #전체 리액션 수  전처리
    if 'reactions' not in post:
        post['count_reactions'] = 0
    else:
        post['count_reactions'] = post['reaction']['summary']['total_count']
    #분석 앞에도 전처리 있고 전처리 꼭 해주자

    #전체 코멘트 수
    if 'comments' not in post:
        post['count_comments'] = 0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']

    #시간대 변경 KST = UTC + 9
    kst = datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')

def crawling(pagename, since, until, fetch=True):
    results = []
    filename = '%s/%s_%s_%s.json' %(RESULT_DIRECTORY, pagename, since, until)

    if fetch:
        for posts in api.fb_fetch_posts(pagename, since, until):
            for post in posts:
                preprocess_post(post)
            results += posts

        # save results to file(저장/적재)
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)   # 리스트 -> json string 변환
            outfile.write(json_string)

    return filename

# def crawling(pagename, since, until, fetch=True):
#     results = []
#     filename = '%s_%s_%s.json' % (RESULT_DIRECTORY, pagename, since)
#
#     for posts in api.fb_fetch_posts(pagename, since, until):
#         # print(posts)
# #for posts in api.fb_f
# # etch_posts("jtbcnews", '2017-01-01', '2017-12-31'):  # yield 문법으로 roop로 돌리기 위함
# #이녀석이 주 코드가 될거임 크롤러에서
#         for post in posts:      # 50개의 개별 data를 전처리해주기 위한 과정
#             preprocess_post(post)
#
#         results += posts    #전처리 된 data가 쌓임
#
#     #save results to file(저장/적재)
#     # open(filename,'w', encoding='utf-8') #쓰기모드로 열어라
#     with open(filename,'w', encoding='utf-8') as outfile:
#         json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)      #json str으로 덤프하는 과정 텝을 4정도 주고 솔팅을 해라 모두 아스키코드로 해라
#         outfile.write(json_string)
#
#     return filename

if os.path.exists(RESULT_DIRECTORY) is False: #import될때 실행됨
    os.makedirs(RESULT_DIRECTORY)     #첫번째 디렉토리가 없으면 하나의 디렉토리가 생성됨
