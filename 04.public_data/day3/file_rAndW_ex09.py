# 파일 닫기

# 1) 일반적인 방법
f=open('test.txt', 'w')
# 파일 작업 수행
f.close()    # 파일 닫음

print('\n')
# 2) 예외처리 : finally 내부
try:
    f=open('test.txt','w')
    # 파일 작업 수행
except:
    # 예외 처리 문장
    print('exception 발생')
finally:
    # 예외가 발생하더라도 반드시 실행
    f.close()

print('\n')
# 3) with 구문
with open('test.txt','w') as f:
    f.write('Hello')

# with 블록을 빠져 나오면 자동으로 파일이 닫힘