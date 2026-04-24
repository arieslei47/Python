#!/usr/bin/python
# coding=utf-8

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def llm_chat(
    model_type : str,
    msg : str,
    system_msg: str = "你是一个通用智能助手",  # 系统提示
    temperature: float = 0.7
) -> str:
    """
        统一LLM调用函数：兼容OpenAI/DeepSeek/通义千问
        :param model_type: 模型类型
        :param msg: 用户输入
        :return: 模型回答
    """

    model_config = {
        "open_ai" : {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "base_url": "https://api.openai.com/v1",
            "model": "gpt-4o"
        },
        "deepseek": {
            "api_key": os.getenv("DEEPSEEK_API_KEY"),
            "base_url": "https://api.deepseek.com",
            "model": "deepseek-chat"
        },
        "tongyi": {
            "api_key": os.getenv("TONGYI_API_KEY"),
            "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
            "model": "qwen-turbo"
        }
    }

    if model_type not in model_config:
        return "不支持的模型类型"

    model = model_config[model_type]

    client = OpenAI(
        api_key=model["api_key"],
        base_url=model["base_url"]
    )

    response = client.chat.completions.create(
        model=model["model"],
        messages=[
            {"role": "system", "content": system_msg},  # 给AI定的身份
            {"role": "user", "content": msg}
        ],
        stream=False,
        reasoning_effort="high",
        temperature=temperature
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    result = llm_chat("deepseek" , "用古典宫廷风，夸我是一个大帅哥" , "你是古代宫廷太监，说话必须用古典宫廷风格，恭敬、华丽")
    print(result)



