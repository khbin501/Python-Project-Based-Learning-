
# print("hi by")

# print("hi 'by'")

# print("hi","by")

# print("hi"+"by")

# print("""hi 

#         by""")

# A = '123'

# # b = "bim"

# C = '12.3'
# print("a = {} b = {}".format(A,C))

# print(f"a = {A} b = {C}")

# x = int(input())
# print(x+5)

# a = [1,2,3,4,5]

# print(a)

# print(a[0])

# print(a[4])

# print(a[:2])

# a.append('hi')

# print(a)

# b = (1,2,3,4,5)

# b.count

# C = {1:a, 2:b, 3:'c'}


# print(C)

# print(C[1],C[2],C[3])


# C.update({5:123.4})

# k = 10

# m = 20

# if k > m:
#         print(f"{k}")
# else:
#         print(f"{m}")

name_list_123 = ['홍','길','동']

for i,k in enumerate(name_list_123):
        print("i =",i," k =",k)

print('5')

test_list = [i*2 for i in range(10)]

print(test_list)

# try:
#         dfcfgdfsd

# except NameError:
#         print("undefined name")
# except TypeErrorr:
#         print('type is wrong')

# else:
#         print("성공")
# finally :
#         print("종료")


def fun1(a,b):
        add = a+b
        mux = a*b
        return add,mux

_,b = fun1(5,3)

print(b)

class Student():
        def __init__(self,name,age,like):
                self.__name = name
                self.__age = age
                self.__like = like
                
        def student_info(self):
                print(f"이름 : {self.__name} 나이 : {self.__age} 흥미 : {self.__like}")

Kim = Student('kim',20,'game')

Kim.student_info()

"""
주석을 주석석석
달아봅시다

"""
import random as rd

print(rd.randint(1,100))
