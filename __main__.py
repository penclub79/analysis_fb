# from analysis_fb.collect import crawler as cw
# cw.crawling("jtbcnews",
#             "2017-01-01",
#             "2017-12-31") #조선, jtbc, 뭐무머뭐 다 적어주면됨 구지 하위파일을 안건들여도됨
# print('run analysis_fb....')

import collect


if __name__ == '__main__':
    items = [
        {'pagename' : "jtbcnews","since": "2017-01-01", "until":"2018-12-31"},
        {'pagename': "chosun", "since": "2017-01-01", "until": "2018-12-31"}
    ]
    #데이터 수집
    for item in items:
        collect.crawling(**item)

    # 데이터 분석(analyze)
    collect.crawling(
        "jtbcnews",
        "2017-01-01",
        "2018-12-31")



    # 데이터 시각화(visualize)