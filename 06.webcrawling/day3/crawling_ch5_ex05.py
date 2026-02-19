# 네이버 뉴스 검색 : 단계 2(1000개 뉴스 검색 및 csv 파일 저장)

import urllib.request
import datetime
import json
import pandas as pd

def get_request_url(url):
    client_id = 'xiGlTRs3W0dQ2bSSAMJP'
    client_secret = 'toy3d6AvDv'

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f"Error for URL: {url}")

def get_naver_search(node, search_text, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'    # 'news'
    query_string = f'{urllib.parse.quote(search_text)}'

    #f'?query={query_string}&start={start}&display={display}'
    parameters = ("?query={}&start={}&display={}".format(query_string, start, display))

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        # JSON 문자열을 Python 객체로 변환
        return json.loads(response)

def get_post_data(post, json_result_list, cnt):    # json_result_list : 리스트의 주소 전달 => call by reference(주소 참조에 의한 호출)
    title=  post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pdate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')

    print(f'[{cnt}]', end=" ")
    print(title, end=' ')
    print(pdate, end=' ')
    print(link)

    # ['번호', '날짜', '제목', '개요', '원본기사링크', '네이버링크']
    json_result_list.append([cnt, pdate, title, description, org_link, link])    # 리스트에 데이터 추가

def main():
    node = 'news'    # 크롤링 대상('blog' 등)
    #search_text = input('검색어를 입력하세요: ')
    search_text = '인공지능'
    cnt = 0
    json_result_list = []

    json_response = get_naver_search(node, search_text, 1, 100)    # 100 : display 개수
    while (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1
            get_post_data(post, json_result_list, cnt)    # json_result_list : 빈 리스트
        
        start = json_response['start'] + json_response['display']    # start : 1, display : 100 그래서 101
        json_response = get_naver_search(node, search_text, start, 100)    # 101번부터 100개 검색

    print(f'전체 검색 수: {cnt}')
    # csv 파일로 저장
    # ['번호', '날짜', '제목', '개요', '원본기사링크', '네이버링크']
    columns = ['count', 'date', 'title', 'description', 'org_link', 'link']
    result_df = pd.DataFrame(json_result_list, columns=columns)
    result_df.to_csv(f'{search_text}_naver_{node}.csv', index=False, encoding='utf-8')

if __name__ == '__main__':
    main()