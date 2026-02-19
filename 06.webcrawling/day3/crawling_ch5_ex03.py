# 네이버 뉴스 검색 : 단계 1(100개의 뉴스 검색 및 json데이터 출력)

import urllib.request
from urllib.parse import quote
import json

def get_request_url(url):
    client_id = 'xiGlTRs3W0dQ2bSSAMJP'
    client_secret = 'toy3d6AvDv'

    req = urllib.request.Request(url)

    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            response_body = response.read()
            return response_body.decode('utf-8')
        else:
            print('Error code: ' + response)

    except Exception as e:
        print(e)
        print(f"Error for URL: {url}")

def get_naver_search(cat, search_text, start, display):    # cat : category 줄임말
    base = 'https://openapi.naver.com/v1/search'    # 15p 참고하면 앞부분은 같아서 base로 담음
    node = f'/{cat}.json'    # 'news'

    query_string = f'{urllib.parse.quote(search_text)}'

    parameters = (f"?query={query_string}&start={start}&display={display}")

    url = base + node + parameters
    response = get_request_url(url)    # 검색결과 저장됨

    if response is None:
        return None
    else:
        # JSON 형식의 문자열을 파싱하여
        # 파이썬의 기본 데이터 타입으로 변환
        return json.loads(response)
    
def main():
    node = 'news'    # 크롤링 대상
    #search_text = input('검색어를 입력하세요: ')
    search_text = '인공지능'
    cnt = 0

    json_response = get_naver_search(node, search_text, 1, 100)
    if (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1
            # 1단계
            print(f'[{cnt}]', end=' ')
            print(post['title'])
            print(post['description'])
            print(post['originallink'])
            print(post['link'])
            print(post['pubDate'])
            # json 데이터 접근, 딕셔너리 형태

if __name__ == '__main__':
    main()