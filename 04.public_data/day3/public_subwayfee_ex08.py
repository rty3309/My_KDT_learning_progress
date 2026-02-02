# 전체 지하철역 승하차 인원 분석 및 파이차트 저장

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

label=['유임승차','유임하차','무임승차','무임하차']
color_list=['#ff9999','#ffc000','#8fd9b6','#d395d0']    # 파이차트 컬러 값
pic_count=0
with open('subwayfee.csv', encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)

    for row in data:
        for i in range(4,8):
            row[i] = int(row[i])    # 원래의 위치에 정수로 변환 후 저장
        print(row)
        plt.figure(dpi=100)    # 저장할 그림파일의 dpi 설정
        plt.title(row[3]+''+row[1])
        plt.pie(row[4:8], labels=label, colors=color_list, autopct='%.1f%%', shadow=True)
        plt.savefig('img/'+row[3]+''+row[1]+'.png')
        plt.close()    # 파일 닫기
        
        # 이 부분만 지우면 전체역(622개) 파이차트 저장됨
        pic_count += 1
        if pic_count >= 10:
            break