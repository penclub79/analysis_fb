import pytagcloud
import os
import collections #count수 셀때 쓰는거
import matplotlib.pyplot as plt  #6/18

RESULT_DIRECTORY = "__results__/visualization"

def wordcloud(filename, wordfreq):
    taglist = pytagcloud.make_tags(wordfreq.items(), maxsize=80)
    # print(taglist)

    save_filename = '%s/word_cloud_%s.jpg' % (RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(
        taglist,
        save_filename,
        size=(900, 600),
        fontname='Malgun',
        rectangular=False,
        background=(0, 0, 0))

def graph_bar(
        title=None,
        xlabel=None,
        ylabel=None,
        showgrid=False,   #grid를 그리지 않겠다
        values=None,
        ticks=None,
        filename=None,
        showgraph=True):  #바그래프그릴때 이함수 쓰면된다
    fig, subplots = plt.subplots(1, 1)  #1개만 그릴거라서 1,1을 씀
    subplots.bar(range(len(values)), values, align='center')#x축,y축 잡아줌

    #ticks
    if ticks is not None and isinstance(ticks, collections.Sequence):
        subplots.set_xticks(range(len(ticks))) #눈금을 몇개로 할건지 #여기 ticks는 클래스 이름
        subplots.set_xticklabels(ticks, rotation=80, fontsize='xx-small')    #라벨링작업   #xticklabels는 메소드 이름

    # title
    if title is not None and isinstance(title, str):
        subplots.set_title(title)

    # xlabel
    if xlabel is not None and isinstance(xlabel, str):
        subplots.set_xlabel(xlabel)

    # ylabel
    if xlabel is not None and isinstance(ylabel, str):
        subplots.set_ylabel(ylabel)


        # show grid 저장하기 전에 데코레이션해야함
    subplots.grid(showgrid)

    if filename is not None and isinstance(filename, str):
        save_filename = '%s/bar_%s.png' % (RESULT_DIRECTORY, filename)
        plt.savefig(save_filename, dpi=400, bbox_inches='tight')   #bbox_inches 여백을 없앰

    #show graph
    if showgraph:   #그래프 그릴건지
        plt.show()
    pass

if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)