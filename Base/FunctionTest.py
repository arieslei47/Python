#!/usr/bin/python
# coding=utf-8

""" python中函数是一等公民 """

# 1. 函数可以被「赋值给变量」
def say_hi():
    print("good morning")

x = say_hi
x()

# 2. 函数可以「放进列表 / 字典」里存着

num_list = [1, 2, 3]
def eat():
    print("干饭")

def sleep():
    print("睡觉")

func_list = [eat , sleep]

func_list[0]()


# 3. 函数可以「当参数传给另一个函数」
def add(x , y):
    return  x * y

def doSomething(func , a ,b):
    result = func(a, b)
    print("result is :", result)

doSomething(add ,10 , 10)


# 4. 函数可以「被另一个函数返回」
def get_sum():
    return 100

def get_fun():
    return say_hi

f = get_fun()
f()

""" 闭包 """
def outer(msg):

    def inner():
        # 内层函数可以引用外层函数的变量msg
        print(f"收到的消息是：{msg}")

    return inner

f1 = outer("hello")
f2 = outer("world")

f1()
f2()






