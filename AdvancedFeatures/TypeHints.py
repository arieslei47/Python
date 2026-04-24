#!/usr/bin/python
# coding=utf-8

import asyncio
from traceback import print_tb

name = "leilei"

# 类型提示
# 1.基础类型提示
name1 : str = "leileige"
age : int = 18


# 2.函数 / 方法提示（最常用）
def get_weather(city : str , weather : str):
    return {'city' : city, 'weather' : weather , "tmep" : 25}

def main():
    res = get_weather("北京","晴")
    print(res)

if __name__ == '__main__':
    main()

# 3.容器类型（列表 / 字典 / 元组）
city : list[str] = ['北京','上海']
weatherlist : dict[str , str] = {'北京' : '晴' , '上海' : '雨'}
tmeptuple : tuple[str , float , float] = ('北京' , 25 , 25.0)

# 4.联合类型（多类型）
def city1(city : str | None) : # 参数可以是 str 或 None
    return city if city else '位置城市'

# 5.异步函数类型提示（实战重点）
# 异步函数：参数str，返回值str
async def async_get_weather(city: str) -> str:
    await asyncio.sleep(1)
    return f"{city} 天气晴朗"

# 异步主函数：无返回值 -> None
async def main2() -> None:
    result : str = await async_get_weather('北京')
    print(result)

