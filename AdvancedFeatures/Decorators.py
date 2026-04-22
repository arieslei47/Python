#!/usr/bin/python
# coding=utf-8

# python 高级特性 ：装饰器 Decorators [ˈdɛkəˌreɪtərz]  带壳瑞兹！！

"""
    1. 装饰器的定义（大白话版）
        装饰器就是一个 “函数增强器”：
        不修改原函数的代码和调用方式；
    给原函数动态添加额外功能（比如日志、计时、权限校验）。
"""
import time
from functools import wraps
from time import sleep


def log(level="INFO"):

    def log_decorator(func):

        # 可变长度参数 写法，*args 和 **kwargs 用来接收任意数量的位置参数和关键字参数
        # *args → 接收的是 没有关键字的参数（位置参数），不管这个参数是数值、字符串还是列表，只要是按顺序传的，都会被它打包成元组
        # **kwargs → 接收的是 带关键字的参数（key = value形式），不管value的类型是什么，都会被它打包成字典。
        # *是解包符号，args是约定俗成的变量名（可以换成其他名字，比如*params）

        @wraps(func)  # 用wraps装饰wrapper，保留原函数元信息
        def wrapper(*args , **kwargs):

            print(f"ready run :{func.__name__}")
            result = func(*args , **kwargs)
            print(f"func: {func.__name__} is done")
            return result

        return wrapper

    return log_decorator

# 语法糖 ↓   等同于 add = log_decorators(add)
# 用装饰器增强add函数：把add传入装饰器，得到增强后的函数
@log()
def add(a , b):
    """ print a + b """
    print("is here")
    return a + b

@log(level="DEBUG")
def add2(a , b , c):
    """ print (a + b) * c"""
    return (a + b) * c

result = add(1 , 2)
print(result)

result2 = add2 (1 , 2 , 3)
print(result2)

# 1.坑点
# 查看函数名：本应是add，结果变成了wrapper
print(add.__name__)  # 输出 wrapper
# 查看文档字符串：本应是上面的注释，结果变成了None
print(add.__doc__)   # 输出 None

# 解决方法：@wraps(func)

print("========= 分隔符：以下为实战内容 =========")


print(" ### 装饰器 - 函数计时 ### ")
# 函数计时装饰器：
def getTime(funct):

    @wraps(funct)
    def ti(*args , **kwargs):

        startTime = time.time()
        result = funct(*args , **kwargs)
        endTime = time.time()
        print(f"函数 {funct.__name__} 运行时长：{endTime - startTime:.4f}秒")
        return result

    return ti

@getTime
def calculateNum(a , b , c , d):
    time.sleep(1)
    z = ( a + b ) * c / d
    return z

var = calculateNum(1 , 2 , 3 , 5)
print(var)

print(" ### 装饰器 - 异常捕获 ### ")







