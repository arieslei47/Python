#!/usr/bin/python
# coding=utf-8


# python中的字典 = json

# dict字典
student = {
    "A" : {
        "age" : 18,
        "height" : 179,
        "weight" : 140
    },
    "B" : {
        "age" : 17,
        "height" : 181,
        "weight" : 125
    },
    "C" : {
        "age" : 19,
        "height" : 182,
        "weight" : 169
    }
}

# 调用方法：

info = student["A"]
print(info)

info2 = student["A"]["age"]
print(info2)
