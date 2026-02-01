# key 매개변수 : 람다식을 활용한 객체 정렬

class Student:
    def __init__(self, name, grade, number):
        # 클래스에 선언된 멤버 변수(self 붙으면 됨)
        self.name = name
        self.grade=grade
        self.number=number

    def __repr__(self):
        return f'({self.name}, {self.grade}, {self.number})'        
    
# Student 객체 리스트 생성
students = [Student('홍길동', 3.9, 20240303),    # Student 객체
            Student('김유신', 3.0, 20240302),    # [Student 객체1, 객체2, 객체3]
            Student('박문수', 4.3,20240301)]    # 객체 배열 형태
print(students[0])

sorted_list=sorted(students, key=lambda s: s.name)    # name 기준으로 정렬
print(sorted_list)