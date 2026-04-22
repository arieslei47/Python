#!/usr/bin/python
# coding=utf-8
from shlex import split

name = "leileige is cool"
age = "18"
score = 100

def listStudy():
    numbers = [3 , 4 , 5 , 8 , 10 , 20]
    print(numbers)
    new = numbers.pop(0)
    print(new)
    print(numbers)
    numbers.reverse()
    print(numbers)

    numbers.sort() # 默认升序
    numbers.sort(reverse=True)

listStudy()

if age >= '18':
    print("您已成年")
else:
    print("您未成年")

if 10 < len(name) < 20:
    print(name.split(" "))

while score > 60 :
    score -= 10
    print(score)





