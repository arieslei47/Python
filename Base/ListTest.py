#!/usr/bin/python
# coding=utf-8

# 外面是list，用 [] 包裹，有序、可修改
# 里面是dict，用 {} 包裹，存储 键值对：key: value
his = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好"},
    {"role": "user", "content": "查询天气"},
    {"role": "assistant", "content": "需要调用天气工具"}
]

def check_len(list1 : list , limit : int = 2) :

    if len(list1) >= limit :
        return list1[-limit:]
    return list1

new_his = check_len(his)
print("截断后上下文：", new_his)


