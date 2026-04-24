#!/usr/bin/python
# coding=utf-8

import asyncio
import time


async def task(name):
    print(f'开始任务：{name}')
    await asyncio.sleep(1)
    print(f'开始任务：{name}')

# 实例1
async def llm_request(model , delay):
    print(f"【请求】{model}")

    await asyncio.sleep(2)  # 模拟调用

    print(f"【完成】{model}")

    return f"{model} 响应成功"

# 实例2，ETL调用各个文件系统的数据
async def get_from_file(file_name):

    print(f"开始抽取文件：{file_name}")
    await asyncio.sleep(2)
    return f"完成抽取文件：{file_name}"


async def get_from_mysql(db):
    print(f"开始拉mysql：{db}")
    await asyncio.sleep(5)
    return f"完成拉mysql：{db}"

async def get_from_redis(rds):
    print(f"开始拉redis：{rds}")
    await asyncio.sleep(3)
    return f"完成拉redis：{rds}"


async def main():
    start = time.time()

    res1, res2 = await asyncio.gather(
        llm_request("gtp4" ,2),
        llm_request("doubao" ,1)
    )

    result = await asyncio.gather(
        get_from_file("a.txt"),
        get_from_mysql("db_order"),
        get_from_redis("rds")
    )

    end = time.time()

    print(f"结果：{res1}, {res2}")

    print(f"结果：{result}")
    print(f'执行时间：{end - start:.2f} s')


    # await asyncio.gather(
    #     task("A"),
    #     task("B")
    # )

asyncio.run(main())



