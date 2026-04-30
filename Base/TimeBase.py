#!/usr/bin/python
# coding=utf-8

from datetime import datetime, timedelta
import time

""" 一、datetime模块 """

# 获取当前**本地时间**（datetime对象）
now = datetime.now()
print("当前本地时间：", now)

print(f"年：{now.year}")
print(f"月：{now.month}")
print(f"日：{now.day}")
print(f"小时：{now.hour}")
print(f"分钟：{now.minute}")
print(f"秒：{now.second}")

# 时间转字符串（datetime -> 字符串）
time_str = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化时间 ：" , time_str)

# 字符串转时间（字符串 → datetime）
str_time = datetime.strptime(time_str ,"%Y-%m-%d %H:%M:%S")
print("转换后的时间对象：" , str_time)

""" 二、time 模块（时间戳 / 延时专用）"""

# 时间戳
timestamp = time.time()  # 1970 年 1 月 1 日到现在的秒数，用于存储/计算时间差等
print("时间戳:" , timestamp)

# 程序延时
time.sleep(1) # 等待1秒

""" 三、高频操作 """

# 时间加减
now = datetime.now()

next_day = now + timedelta(days=1) # 加1天
next_hour = now + timedelta(hours=2) # 加2小时
next_min = now - timedelta(minutes=30) # 减30分钟

print(f"next_day : {next_day} \nnext_hour : {next_hour} \nnext_min : {next_min}")

# 计算时间差
t1 = datetime.now()
t2 = datetime.now() + timedelta(hours=2)

diff = t2 - t1
print(f"时间差：{diff}")
print(f"相差秒数：, {diff.seconds}")  # 秒
print(f"相差天数：, {diff.days}")  # 天

# 时间戳 ↔ datetime 互转
# 时间戳 → datetime
ts = time.time()
dt = datetime.fromtimestamp(ts)
print("时间戳转时间：", dt)

# datetime → 时间戳
now = datetime.now()
ts = now.timestamp()
print("时间转时间戳：", ts)















