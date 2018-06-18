from analysis_fb.collect.api import api

# url = api.fb_gen_url(node='jtbcnews', a=10, b=20, s='kickscar')
# print(url)

# id= api.fb_name_to_id("jtbcnews")
# print(id)

# api.fb_fetch_posts("jtbcnews", '2017-01-01', '2017-12-31') #루프없이 결과 돌리기
# results = api.fb_fetch_posts("jtbcnews", '2017-01-01', '2017-12-31') # api.py While roop로 돌리기 위함
# print(results)
for posts in api.fb_fetch_posts("jtbcnews", '2017-01-01', '2017-12-31'):  # yield 문법으로 roop로 돌리기 위함
    print(posts)


#url 만드는 작업