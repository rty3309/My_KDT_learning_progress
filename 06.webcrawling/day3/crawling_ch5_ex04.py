# 네이버 뉴스 검색 : 단계 2(1000개 뉴스 검색)
# datetime 변환

import datetime

date_string = "Tue, 13 Aug 2024 09:02:00 +0900"    # 원본 문자열 => datetime 변환

# strptime(string, format): string -> datetime 변환
pdate = datetime.datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S +0900')    # date_string의 현재 구성목록(순서)
print(f'{type(pdate)}: {pdate}')

# strftime(format): datetime -> string 변환
pdate_string = pdate.strftime('%Y-%m-%d %H:%M:%S')
print(f'{type(pdate_string)}: {pdate_string}')
