#!/usr/bin/python
# coding=utf-8

from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载.env文件中的环境变量
load_dotenv()

# 读取密钥
#openai_api_key = os.getenv("OPENAI_API_KEY")
api_key = os.getenv("DEEPSEEK_API_KEY")
#tongyi_api_key = os.getenv("TONGYI_API_KEY")

# 2. 初始化客户端（标准写法）
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
    # base_url默认是https://api.openai.com/v1，无需手动写
)

# 3. 调用模型
# noinspection PyTypeChecker
response = client.chat.completions.create(
    model="deepseek-v4-pro",  # 模型名称
    messages=[
        {"role": "system", "content": "你是专业编程助手"},
        {"role": "user", "content": "PydanticV2详解"}
    ],
    stream=False,
    reasoning_effort="high",
    extra_body = {"thinking": {"type": "enabled"}}
)

# 4. 打印结果
print("DeepSeek 回答：", response.choices[0].message.content)
