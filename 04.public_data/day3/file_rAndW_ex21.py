import pickle
class Person(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return f'({self.id}, {self.name})'
    
p1 = Person(1, 'Kim')
p2 = Person(2, 'Park')
p3 = Person(3, 'Lee')

person_list = [p1, p2, p3]
# 객체 리스트를 파일로 저장
fname = 'person.pickle'
fout=open(fname, 'wb')
pickle.dump(person_list, fout)    # person_list : 3개의 객체를 가지는 리스트
fout.close()

# 파일의 내용을 객체 리스트로 읽어옴
fin = open(fname, 'rb')
plist = pickle.load(fin)
print(plist)
fin.close()    # 출력은 __repr__dp 에 정의된 형태로 출력