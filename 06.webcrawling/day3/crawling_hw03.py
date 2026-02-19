# Crawling 과제 #3
# KDT 12기 이재헌

# 과제 3 : 네이버 증시 정보 크롤링

import pandas as pd
from bs4 import BeautifulSoup
import requests

def stock_top10_ranks():
    url = 'https://finance.naver.com/sise/sise_market_sum.naver'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    stock_top10_list = []
    stocks = soup.find_all('a', class_='tltle')

    for i in range(10):
        name = stocks[i].text
        link = stocks[i]['href']
        stock_top10_list.append({'name': name, 'link': link})
    return stock_top10_list
    
def get_stock_data(top10_list):
    base_url = 'https://finance.naver.com'
    all_stocks = []

    for i in range(10):
        detail_link = base_url + top10_list[i]['link']    # 링크
        stock_code = top10_list[i]['link'].split('=')[-1]    # 종목코드
        
        res = requests.get(detail_link)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, 'html.parser')

        currentP = soup.select_one(".no_today .blind").text
        info = soup.select(".no_info tr")
        
        previousP = info[0].select(".blind")[0].text    # 전일
        highestP = info[0].select(".blind")[1].text    # 고가
        openingP = info[1].select(".blind")[0].text    # 시가
        lowestP  = info[1].select(".blind")[1].text    # 저가

        stock_info = {'링크' : detail_link,
                    '종목명': top10_list[i]['name'],
                    '종목코드': stock_code,
                    '현재가': currentP,
                    '전일': previousP,
                    '고가': highestP,
                    '시가': openingP,
                    '저가': lowestP}
        
        all_stocks.append(stock_info)
    return pd.DataFrame(all_stocks)

def print_stock(row):
    for key, value in row.items():
        if key == '링크':
            print(f"{value}")
        else:
            print(f"{key}: {value}")      

def main():
    top10_list = stock_top10_ranks()
    stock_df = get_stock_data(top10_list)

    while True:
        print('-'*30)
        print('[네이버 코스피 상위 10대 기업 목록]')
        print('-'*30)
        for i in range(10):
            print(f'[{(i+1):2d}] {top10_list[i]['name']}')
        search = int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))
        
        if 1 <= search <= 10:
            print_stock(stock_df.iloc[search-1])
        elif search == -1:
            print('프로그램 종료')
            break
        else:
            print('잘못된 번호를 입력하였습니다. 다시 입력하세요.')

if __name__ == '__main__':
    main()