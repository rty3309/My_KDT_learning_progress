# 딕셔너리에 lambda 적용 예제

# 딕셔너리 생성
import pandas as pd

addr_aliases={'경기':'경기도', '경남':'경상남도','경북':'경상북도',
             '충북':'충청북도', '서울시':'서울특별시', '부산특별시':'부산광역시',
             '대전시':'대전광역시','부산시':'부산광역시','충남':'충청남도', '전남':'전라남도', '전북':'전라북도'}

# dict.get(key) : 'key'에 대응하는 값이 없으면 None을 리턴
print(addr_aliases.get('경기'))
print(addr_aliases.get('대전'))    # None을 리턴
print(addr_aliases.get('부산'))    # '부산' key는 없음
print(addr_aliases.get('부산','부산광역시'))    # key에 '부산'이 없으면 '부산광역시' 리턴
                              #'부산광역시' : default값 지정

print('\n')
# DataFrame 생성
addr_df = pd.DataFrame(['경기','대전광역시','경남','경북','충북','충남','전북','전남','경상북도'], columns=['시도'])
print(addr_df)

print('\n')
# lambda v: dict.get(key, default) 사용
# dictionary에서 key에 해당하는 값이 없으면, default에 지정한 값을 리턴
addr_df['시도']=addr_df['시도'].apply(lambda v: addr_aliases.get(v,v))    # get(v,v) : key값을 default 값으로 
print(addr_df)

print('\n')
# lambda v : addr_aliases.get(v, v)를 일반 함수로 구현
def get_dict_value(key):
    if not addr_aliases.get(key):
        print('key:{}에 해당되는 값이 없어서 {}를 반환함'.format(key,key))
        return key
    else:
        value= addr_aliases.get(key)
        #print('key:{}, value:{}'.format(key,value))
        return value

print(get_dict_value('대구'))

print('\n')
# DataFrame에 apply(get_dict_value) 적용
addr_df1=pd.DataFrame(['경기','대전광역시','경남','경북','충북','충남','전북','전남','경상북도'], columns=['시도'])

# lambda식 대신에. get_dict_value()함수 호출
addr_df1['시도']=addr_df1['시도'].apply(get_dict_value)
addr_df1