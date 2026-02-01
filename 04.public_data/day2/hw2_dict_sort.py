# Python 과제 #2
# KDT 12기 이재헌

# 1. 딕셔너리 생성 및 정렬 프로그램

def dict_sort(data, key_func, reverse=False):
    return sorted(data.items(), key=key_func, reverse=reverse)

def main():
    country = {"Seoul":['South Korea', 'Asia', 9655000],
               "Tokyo":['Japan', 'Asia', 14110000],
               "Beijing":['China', 'Asia', 21540000],
               "London":['United Kingdom', 'Europe', 14800000],
               "Berlin":['Germany', 'Europe', 3426000],
               "Mexico City":['Mexico', 'America', 21200000]}

    while True:
        print('-' * 40)
        print('1. 전체 데이터 출력')
        print('2. 수도 이름 오름차순 출력')
        print('3. 모든 도시의 인구수 내림차순 출력')
        print('4. 국가명 오름차순 출력')
        print('5. 특정 도시의 정보 출력')
        print('6. 대륙별 인구수 계산 및 출력')
        print('7. 프로그램 종료')
        print('-' * 40)

        menu = input('메뉴를 입력하세요: ')
        
        if menu.isdigit():
            menu = int(menu)
        else:
            menu = 0

        if menu == 1:
            for i, (city, info) in enumerate(country.items(), start=1):
                print(f"[{i}] {city}: {info}")

        elif menu == 2:
            res = dict_sort(country, lambda x: x[0])
            for i, (city, info) in enumerate(res, start=1):
                print(f"[{i}] {city} : {info[0]} {info[1]} {info[2]:,}")

        elif menu == 3:
            res = dict_sort(country, lambda x: x[1][2], reverse=True)
            for i, (city, info) in enumerate(res, start=1):
                print(f"[{i}] {city} : {info[2]:,}")

        elif menu == 4:
            res = dict_sort(country, lambda x: x[1][0])
            for i, (city, info) in enumerate(res, start=1):
                print(f"[{i}] {city} : {info[0]}")

        elif menu == 5:
            search_city = input('조회할 도시 이름을 입력하세요: ')
            if search_city in country:
                info = country[search_city]
                print(f'국가: {info[0]}, 대륙: {info[1]}, 인구수: {info[2]:,}')
            else:
                print(f'도시이름:{search_city}은 key에 없습니다.')

        elif menu == 6:
            continent = input('대륙 이름을 입력하세요(Asia, Europe, America): ')
            target_list = list(filter(lambda x: x[1][1].lower() == continent.lower(), country.items()))
            total_pop = 0
            for city, info in target_list:
                print(f'{city} : {info[2]:,}')
                total_pop += info[2]
            print(f'{continent} 전체 인구수: {total_pop:,}')
            
        elif menu == 7:
            print('프로그램을 종료합니다.')
            break

        else:
            print('** 주의! 메뉴의 항목이 아닙니다. **')

main()