# http test
import sys
from urllib.request import Request, urlopen  #모듈 가져오기
from datetime import *
#
# url = 'http://www.naver.com'
# request = Request(url)    #리퀘스트 객체 생성

try:
    url = 'http://www.naverewq.com'
    request = Request(url)

    url = 'http://www.naver.com'
    urlopen(request)
    resp = urlopen(request) #응답 받기
    resp_body = resp.read().decode("utf-8")            #응답 읽기 (바디 내용)  - 바이트로 통신    인코딩 했으면 디코딩도 해야함
    print(resp_body)    #네이버 바디(코드)를 가져옴
except Exception as e:
    print('%s %s' % (e, datetime.now()), file = sys.stderr)

"""
System.out.println('HelloWorld'); = sys.stderr
write
"""
#html 받앗음