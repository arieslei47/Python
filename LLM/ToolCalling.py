#!/usr/bin/python
# coding=utf-8
import os

from dotenv import load_dotenv
# 1. 工具装饰器
from langchain.tools import tool
# 2. 工具调用Agent
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
# 3. 提示词模板（1.x版本和之前一样）
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

# 4. DeepSeek兼容OpenAI客户端
from langchain_openai import ChatOpenAI

load_dotenv()

deepseek = os.getenv("DEEPSEEK_API_KEY")

# 第一步：自定义一个工具 Tool
# 就这一个函数，就是今天学的「搜索Tool」
@tool   # 标记：这是一个可以给大模型调用的工具
def web_search(query : str) -> str :
    """
        这段文字超级重要！！
        大模型看不懂代码，只能看懂这段文字描述
        大模型靠这段文字判断：什么时候该用这个工具

        功能：获取最新、未来、大模型不知道的外部数据
    """
    print(">>> 正在执行搜索工具，参数：", query)
    return "2026年LangGraph市场占比约28%，行业第二。"

# 第二步：连接 DeepSeek 大模型
llm = ChatOpenAI(
    model = "deepseek-chat",
    api_key = deepseek,
    base_url = "https://api.deepseek.com",
    temperature=0  # 0=不瞎编，工具调用必须开0
)

# 第三步：把工具打包，告诉大模型：你可以用这个工具
tools = [web_search]

# 第四步：简单提示词
# 这行代码 = 给 AI Agent 写「固定剧本 + 严格规矩」
# 是 LangChain Tool Calling 必须这么写的固定格式，少一行都跑不起来！
prompt = ChatPromptTemplate.from_messages([
    # system（系统提示词）：给 AI 定铁规矩
    ("system", "你必须依靠工具返回的数据回答，不能瞎编"),
    # human（用户输入）= 放你的问题
    ("human", "{input}"),
    # agent_scratchpad = AI 的草稿本 / 记事本（最难懂、最关键）
    # 大白话翻译：
    # “AI，我把你刚才调用工具的所有记录、搜索到的数据，
    # 全都放在这个草稿本里了，你看着这个本子回答！”
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# ======================
# 第五步：创建工具调用控制器
# ======================
# 绑定大模型+工具，让大模型拥有调用工具的能力
agent = create_tool_calling_agent(llm, tools, prompt)
# 执行器：负责解析大模型的调用指令、自动运行工具
# verbose=True 干嘛？控制台打印全过程：
# 大模型什么时候决定调用工具、传了什么参数，方便你看懂流程。
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


if __name__ == "__main__":
    res = agent_executor.invoke({"input": "2026年LangGraph市场占比"})
    print("\n最终回答：", res["output"])







