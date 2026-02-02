# lambda와 operator를 사용한 dictionary 정렬

names={'Mary':10999, 'Sams':2111,'Aimy':9778,'Tom':20245,'Michale':27115,'Bob':5887, 'Kelly':7855}
print(names.items())
print()

# Key를 기준으로 정렬(기본: 오름차순)
print('[lambda] dict 정렬: key 기준 오름차순')
res=sorted(names.items(), key=(lambda x: x[0]))
print(res)
print()

# Value를 기준으로 정렬, 내림차순: reverse=True
print('[lambda] dict 정렬: value 기준, 내림차순')
res=sorted(names.items(), key=(lambda x: x[1]), reverse=True)
print(res)