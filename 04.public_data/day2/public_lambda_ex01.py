# key 매개변수

msg='The health know not of their health, but only the sick'
sorted_list = sorted(msg.split(), key=str.lower)    # str.lower : 문자열을 소문자로 변경 후 정렬
# msg.split() : 문자열 분리, key=str.lower : 문자열 소문자 변경 함수, 소문자 기준 오름차순
# 내부적으로 정렬만 소문자로 바꿔서 한 것 뿐이라 출력은 대문자 그대로 출력됨.
print(sorted_list)

# 문자열의 길이를 기준으로 내림차순 정렬
msg='The health know not of their health, but only the sick'
descending_sorted_list=sorted(msg.split(), key=len, reverse=True)    # 문자열 길이의 역순
print(descending_sorted_list)