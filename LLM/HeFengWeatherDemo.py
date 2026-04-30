#!/usr/bin/python
# coding=utf-8

import os

import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from pydantic import BaseModel , Field

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    api_key = os.getenv('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com/",
    temperature=0
)

# pydantic
class CheckParm(BaseModel) :
    city : str = Field(description="需要查询的城市名称，例如：北京、上海、重庆")

# args_schema ： 参数校验规则，让大模型只能按规矩传参，不准乱传！
@tool(args_schema=CheckParm)
def hefeng_weather(city : str) -> str :

    """
        查询指定城市的实时、历史天气，包括天气状况和当前温度。
        参数：city - 城市名称，例如：北京、上海、重庆
    """

    """查询指定城市的天气"""
    try:
        key = os.getenv('HEFENG_API_KEY')
        api_host = 'ny6heyhcgu.re.qweatherapi.com'
        print(f"【调试】使用的和风Key: {key}")  # 打印Key，排查是否正确

        # 1. 请求城市ID
        city_url = f"https://{api_host}/geo/v2/city/lookup?location={city}&key={key}"
        resp = requests.get(city_url, timeout=10)

        # 🔥 关键：打印原始返回内容，看API返回了啥
        print(f"【调试】城市API返回: {resp.text}")

        # 先判断状态码，再解析JSON
        if resp.status_code != 200:
            return f"API请求失败，状态码：{resp.status_code}"

        city_data = resp.json()

        # 判断和风返回的业务状态码
        if city_data.get("code") != "200":
            return f"城市查询失败，错误码：{city_data.get('code')}"

        location_id = 0

        for city in city_data['location'] :
            if city['name'] == '北京' :
                location_id = city['id']
                break

        todayis = datetime.now() + timedelta(days=-1)
        dateis = todayis.strftime("%Y%m%d")
        print("昨天时间")

        # 2. 请求天气
        #weather_url = f"https://{api_host}/v7/weather/now?location={location_id}&key={key}"
        weatherHis_url = f"https://{api_host}/v7/historical/weather?location={location_id}&date={dateis}&key={key}"
        weather_resp = requests.get(weatherHis_url, timeout=10)
        print(f"【调试】天气API返回: {weather_resp.text}")

        weather_data = weather_resp.json()
        now = weather_data["now"]

        return f"{city}：{now['text']}，温度：{now['temp']}℃"

    except Exception as e:
        return f"工具执行失败：{str(e)}"

    # # 官方API，获取城市id
    # city_url = f"https://geoapi.qweather.com/v2/city/lookup?location={city}&key={os.getenv('HEFENG_API_KEY')}"
    # city_data = requests.get(city_url).json()
    # location_id = city_data["location"][0]["id"]
    #
    # weather_url = f"https://devapi.qweather.com/v7/weather/now?location={location_id}&key={os.getenv('HEFENG_API_KEY')}"
    # weather_data = requests.get(weather_url).json()
    # now = weather_data["now"]
    #
    # return f"{city} : {now['text']} , 温度：{now['temp']}"

tools = [hefeng_weather]

prompt = ChatPromptTemplate.from_messages ([
    ("system" , "你是一个天气小助手"),
    ("user" , "{input}"),
    MessagesPlaceholder("agent_scratchpad")
])

agent = create_tool_calling_agent(llm , tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__" :
    res = agent_executor.invoke({"input":"查询昨天北京天气"})
    print(res["output"])









