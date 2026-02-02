# 디렉토리 작업 예제

import os

dir = os.getcwd()
print(dir)

subdir = 'data'    # data 폴더 내 읽어옴
os.chdir(subdir)
print(os.getcwd())

for filename in os.listdir():
    print(filename, end='')
    if os.path.isfile(filename):
        print(': 파일')
    elif os.path.isdir(filename):
        print(': 디렉토리')