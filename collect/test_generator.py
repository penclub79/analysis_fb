def squares(n=10): #10까지 자승하는애
    results = []    #list로 받기여
    for i in range(n+1):
        # results.append(i**2)
    # return i**2     #return은 한번만 호출하고 만다 그래서 yield를 쓴다 루프가 끝날때까지 바깥에다가 던져줌
        yield i**2
# squares(10)
# 0~10까지 호출해봄


for x in squares(10):
    print(x)

# results = squares(10) 같은 방법
# for x in results:
#      print(x)