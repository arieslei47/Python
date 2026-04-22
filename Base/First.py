#!/usr/bin/python
# coding=utf-8
# -*- coding: UTF-8 -*-
import sys

aa=0
print (aa)

# raw_input("按下 enter 键退出，其他任意键显示...\n")

x='roobot'
sys.stdout.write(x + '\n')

abc= 1000000000000000000000000000000000000000000000000000
print(abc)

lst = [1,2,3,"leilei",True]
print(lst)
lst.append(4)
print(lst)
lst.insert(1,"在1位插入")
print(lst)
print (lst[::2])

print("==================")

# 常用方法get(), keys(), values(), items(), update(), pop()
# items() —— 获取所有键值对
# 作用：把字典里所有的键值对变成一个可迭代的对象（Python 3 中是 dict_items 类型），常用于 for 循环同时遍历 key 和 value。

d= {"name": "leilei", "age": "18", "city": "BeiJing", "score": 100}
print(d.get("age"))
print(d.keys())
for k,v in d.items():
    print(k,v)

# update() —— 更新/合并字典
# 作用：把另一个字典（或键值对）合并到当前字典里，如果 key 已经存在就覆盖原来的值。
d.update({'money': "100000.9999", 'sex': 1, 'score': 99.99})
print(d)

# 方法2：直接用 key=value 形式（更方便）
d.update(city="New York", hobby="Python")
print(d)

# pop() —— 删除指定键并返回它的值
# 删除字典中某个 key，同时把对应的值返回给你。
# 返回值：被删除 key 对应的值（如果 key 不存在且没给 default，会报 KeyError）
d.pop("hobby")
print(d)

# key 不存在时，给 default 防止报错
score = d.pop("high", 0)   # 不存在就返回 0
print(score)      # 0
print(d)          # 字典不变

fs = frozenset

print("==================")











