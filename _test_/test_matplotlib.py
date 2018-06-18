import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from numpy.random import randn



def ex1():
    # plt.plt([1, 2, 3, 4], [10, 20, 30, 40])
    plt.plot([10, 20, 30, 40])
    plt.show()

#피규어
def ex2():
    fig = plt.figure()
    sp1 = fig.add_subplot(2, 1, 1)
    sp1.plot([1, 2, 3, 4], [10, 20, 30, 40])

    sp2 = fig.add_subplot(2, 1, 2)
    sp2.plot([1, 2, 3, 4], [100, 200, 300, 400])

    plt.show();

def ex3():
    fig=plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(randn(50).cumsum(), 'k--')

    sp2=fig.add_subplot(2, 2, 2)
    sp2.hist(randn(1000), bins=20, color='k', alpha=0.3)

    sp3 = fig.add_subplot(2, 2, 3)
    sp3.scatter(np.arange(100), np.arange(100)+3*randn(100))

    plt.show()

def ex4():
    fig, subplot = plt.subplots(1,1)    #튜플을 리턴한다.
    subplot.plot([10, 20, 30, 40])
    plt.show()

def ex5():
    plt.subplots(2, 2, sharex=True, sharey=True)
    for i in range(2):
        for j in range(2):
            subplots[i, j].hist(randn(randn(100), bins=20, color='k', alpha=0.3))
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()

def ex6():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot([1, 2, 3, 4], [10, 20, 30, 40], 'go--')
    plt.show()

def ex7():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot([1, 2, 3, 4],
                 [10, 20, 30, 40],
                 color='g',
                 linestyle='--',
                 marker='o')
    plt.show()


def ex8():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot(
        [1, 2, 3, 4],
        [10, 20, 30, 40],
        color='#335599',
        linestyle='solid',
        marker='v')

    plt.show()

def ex9():
    fig, subplot = plt.subplots(1,1)
    data = randn(50).cumsum()
    subplot.plot(data, color='black', linestyle='dashed', label='AAA')
    subplot.plot(data, color='blue', drawstyle='steps-mid', label='BBB')

    plt.legend(loc='best')
    plt.show()

def ex10():
    fig, subplot = plt.subplots(1,1)
    subplot.plot(randn(1000).cumsum())
    subplot.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900])

    plt.show()

def ex11():
    fig, subplot = plt.subplots(1,1)
    subplot.plot(randn(1000).cumsum())
    subplot.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900])
    subplot.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5','pt6','pt7','pt8','pt9','pt10'],
        rotation=30,
        fontsize='small')

    subplot.set_xlabel('Points')
    subplot.set_title('Matplotlib Test')

    plt.show()

def ex12():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(1000).cumsum(), 'k', label='one')
    subplots.plot(randn(1000).cumsum(), 'k-.', label='two')
    subplots.plot(randn(1000).cumsum(), 'k.', label='three')

    plt.legend(loc='best')
    plt.show()

#한글 깨지는거 처리함
def ex13():
    # font_filename = 'c:/Windows/fonts/malgun.ttf'
    # font_name = font_manager.FontProperties(fname=font_filename).get_name()
    # print(font_name) #폰트 네임이 뭔가 알려고
    font_options = {'family': 'Malgun Gothic'}
    plt.rc('font', **font_options)
    plt.rc('axes', unicode_minus=False)


    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='기본')
    subplots.plot(randn(1000).cumsum(), 'k--', label='대시')
    subplots.plot(randn(1000).cumsum(), 'k.', label='점')

    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small')
    subplots.set_xlabel('포인트')
    subplots.set_title('예제12 한글처리')
    plt.legend(loc='best')

    plt.show()

if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    ex13()
