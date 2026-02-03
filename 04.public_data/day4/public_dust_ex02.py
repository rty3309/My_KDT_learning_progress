# 미세먼지 데이터 전처리 : 시간 오류 수정 및 파일 저장

import pandas as pd
from datetime import timedelta

def zerofrom24(datestring):
    '''
    24시로 표현된 값을 익일 00로 변환
    '''
    try:
        return pd.to_datetime(datestring, format='%Y-%m-%d %H')    # 시간정보 0~23시까지는 정상 처리됨
    except:    # 핵심부분
        datestring = datestring[:11] + '00'    # 시간정보에 '24' 포함하면 try에서 처리 안 되고 except 처리로 옴
        return pd.to_datetime(datestring, format='%Y-%m-%d %H') + timedelta(days=1)
    
dust=pd.read_excel('dust.xlsx')
dust.rename(columns={'날짜':'date', '아황산가스':'so2', '일산화탄소':'co',
                     '오존':'o3', '이산화질소':'no2'}, inplace=True)
dust['date']=dust['date'].apply(zerofrom24)    # 'date' 문자열 : datestring
print(dust.info())
print(dust[dust['date'].dt.day==2])

dust.to_excel('dust_hour.xlsx', index=False)
print('DataFrame을 excel로 저장 완료')