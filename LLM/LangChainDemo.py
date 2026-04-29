#!/usr/bin/python
# coding=utf-8

import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

""" 最简单的一个LangChain Demo ，没有工具的写法 """

load_dotenv()

ds_api = os.getenv("DEEPSEEK_API_KEY")

# ChatOpenAI() = 对话模型（你现在必须用的） 对应 Chat Completions API，专门做聊天、Agent、Tool Calling、多轮对话
# OpenAI() = 文本补全模型（老古董，几乎淘汰） 对应 Completions API，专门做文本续写、补全句子，不能做 Agent
llm = ChatOpenAI(
    model = "deepseek-v4-flash",
    api_key = ds_api,
    base_url = "https://api.deepseek.com",
)

# 对话提示模板  prompt ：提示  Template : 模版
def prompt1(systemin : str = "你是一个通用的AI助手") :
    prompt = ChatPromptTemplate.from_messages([
        ("system" , f"{systemin}"),
        ("user" , "{input}")
    ])
    return prompt

# StrOutputParser() 是 LangChain 的输出解析器
# 作用：把大模型返回的复杂对象，转换成我们能直接用的纯文本字符串（str）
chain = prompt1("你是一个生活小管家") | llm | StrOutputParser()

result =  chain.invoke({"input" : "上海未来20天天气如何？"})

print(result)

