#!/usr/bin/python
# coding=utf-8

from datetime import datetime
from pydantic import BaseModel, field_validator
import re

"""
    手写题：定义一个用户注册模型 UserRegister，满足以下要求（大厂高频）
    需求
        用户名 username：必填，字符串，长度 3~15 位，不能包含特殊字符；
        密码 password：必填，字符串，长度≥8 位，必须包含字母 + 数字；
        邮箱 email：必填，合法邮箱格式；
        注册日期 register_date：可选，默认当前日期，格式 YYYY-MM-DD，不能晚于今天；
        手机号 phone：可选，合法手机号格式（11 位数字，以 1 开头）。
"""

class CheckUser(BaseModel):

    username: str
    password: str
    email: str
    register_date: str = datetime.now().strftime("%Y-%m-%d")
    phone: int

    @field_validator("username")
    def checkUserName(cls , value : str) -> str:
        value = value.strip()

        if not 3 <= len(value) <= 15:
            raise ValueError("字符串长度不符")
        if not re.match(r"^[a-zA-Z0-9_]+$", value):  #Python 自带的正则表达式模块
            raise ValueError("不能带特殊字符")

        return value

    #@field_validator("password")
    #def checkPassWord(cls , value : str) -> str:





