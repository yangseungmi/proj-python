
"""
a= "{0:<10}".format("hi")
b=f'{"bhc":^^10}'
print(a+"33")
print(b)
c='  bh d  d '.strip()
print(c,42)
d=[1,2,3]
d.append([4,5])
print(d)

str=['a','b','c']
print(str.index('b'))
print(str[2])
str.insert(0,'first') 
print(str)
str.remove('a')
print(str)

dic ={'m':3,"n":"p"}
print(dic.values())
print(list(dic.keys()))

isInvlole ='ms' in dic
print(isInvlole)

s1 = set([1,2,3])
s1.remove(3)
print(type(s1))

pin="931103-2184219"
print('19'+pin[:6])

marks = [11,22,33,32]
for num in range(len(marks)):
     if marks[num] >30:
          print("%d번 과목 점수는 %d이고 합격" % (num+1,marks[num]))
     else:
         print("%d번 과목은 %d 차이로 탈락" % (num+1, 30-marks[num]))


sum = 0;
for i in range(1, 101):
        sum += i
print("sum:", sum)



for a in range(2,10):
    for b in range(1,10):
        print(a,"*",b,"=",a*b, end=" ,,")
    print("/")
print("="*10)



result = 0
i = 1
while i <= 1000:
    if i % 3 >0: 
        pass 
    else: 
        result +=i
    i +=1
print(result)

add = lambda a,b : a+b
print(add(3,2))

f=open("newFile.txt","a")
f.write('test1')
f.write('test2')
f.close()

f1 = open("newFile.txt","r")
while 1:
    line =f1.readline()
    if not line: break
    print(line)


f1 = open("newFile.txt","r")
lines = f1.readlines()
for l in lines:
    print("yy",l)
f1.close()

with open("newFile.txt", "a") as f:
    f.write("124")

## 대문자로 만들기 스크립트₩
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=" ")


def isPalindrom(x):    
    half = len(str(x))//2
    for i in range(1,half):
        t1 = x[:i]
        t2 = x[i:].reverse
        if t1 == t2:
            return True
        else:
            return False

print(isPalindrom(1213))


a=[1,2]
print("first",a[::-1])
print(a[::0])
print(a[::1])
print(a[::2])


a= dict()
a[('b',)] = 'python'
print(a)
"""

a=[1,2,3,3,3]
aSet = set(a)
print(aSet)
b = list(aSet)
print(b)