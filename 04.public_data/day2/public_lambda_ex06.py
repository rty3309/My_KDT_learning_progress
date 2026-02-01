# map 함수

def square(n):
    return n*n

mylist=[1,2,3,4,5]
result=list(map(square, mylist))    # mylist : 생성자
print(result)

int_list=list(map(int, input('정수를 입력하세요: ').split()))
print(int_list)

# 간단한 딕셔너리에 lambda 적용
d={'a':1,'b':2}

# map의 첫 번째 파라미터 function은 lambda 함수로 대체
values=map(lambda key: d[key],d.keys())    # map(함수, iterable 객체)
print(list(values))    # 딕셔너리에서 값만 받아와서 리스트로 만듬

list_369=list(map(lambda x:'짝'if x %3 ==0 else x, range(1,10)))
print(list_369)