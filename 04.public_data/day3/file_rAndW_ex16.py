# csv 파일에 저장 : csv.writer()

import csv

f=open('output.csv','w', encoding='utf-8', newline='')

writer = csv.writer(f)
writer.writerow([1, 'Alice', True])
writer.writerow([2,'Bob', False])

f.close()