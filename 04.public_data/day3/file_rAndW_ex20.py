# 딕셔너리 파일 입출력 예제

import pickle

fout =open('pickle.bin', 'wb')
mydict= dict()


mydict['a']=1
mydict['b']=10
mydict['c']=100

pickle.dump(mydict, fout)
fout.close()

fin=open('pickle.bin','rb')    # rb : read binary
dict1= pickle.load(fin)
fin.close()
print(dict1)