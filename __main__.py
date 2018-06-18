# from analysis_fb.collect import crawler as cw
# cw.crawling("jtbcnews",
#             "2017-01-01",
#             "2017-12-31") #조선, jtbc, 뭐무머뭐 다 적어주면됨 구지 하위파일을 안건들여도됨
# print('run analysis_fb....')

import collect
import analyze
import visualize

if __name__ == '__main__':
    items = [
        {'pagename' : "jtbcnews", "since": "2017-01-01", "until":"2018-12-31"},
        {'pagename': "chosun", "since": "2017-01-01", "until": "2018-12-31"}
    ]
    #데이터 수집
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile

    # 데이터 분석
    # for item in items:
    #     print(item['resultfile'])
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)
        # print(data)
        print(item['count_wordfreq'])
        # item['count_wordfreq'] = analyze.count_wordfreq(data)
    #     위의 count_wordfreq는 빈도분석
    # collect.crawling(
    #     "jtbcnews",
    #     "2017-01-01",
    #     "2018-12-31")

    # 데이터 시각화(visualize)
    for item in items:
        count = item['count_wordfreq']
        count_m50 = dict(count.most_common(50))

        filename = '%s_%s_%s' % (item['pagename'], item['since'], item['until'])
        visualize.wordcloud(filename, count_m50)
        # visualize.graph_bar()
