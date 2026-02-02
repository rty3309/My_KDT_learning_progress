# zip() 함수

numbers=[1,2,3,4]
letters=['A','B','C','D']
for pair in zip(numbers, letters):    # 하나로 묶어서 출력
    print(pair)

pair = list(zip(numbers, letters))
print(pair)

numbers, letters=zip(*pair)    # zip 해제 : * (아스타리스크(asterisk)) 사용
print(numbers, letters)