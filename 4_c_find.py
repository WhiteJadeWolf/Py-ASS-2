""" Write a program to implement the string find method without using predefined functions """

def FIND(x,str1,start=0,end=999999):
    str=str1[start:end]
    ns,nx=0,0
    for i in str:
        ns+=1
    for i in x:
        nx+=1
    for i in range(ns):
        if x==str[i:i+nx]:
            return i
    else:
        return -1

# test
print(FIND('a','cat'))
print(FIND('bcd','abcde'))
print(FIND('bcd','abcde',0,2))
print(FIND('q','abcde'))
print(FIND('bcd','abcde',0,4))