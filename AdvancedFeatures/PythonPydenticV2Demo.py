#!/usr/bin/python
# coding=utf-8

from datetime import datetime

from pydantic import BaseModel, field_validator, model_validator
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
    phone: str | None = None    # 单一个None 表示可以不传值，两个None表示，可以不传值，不传值值为空

    @field_validator("username")
    def checkUserName(cls , value : str) -> str:
        value = value.strip()

        if not 3 <= len(value) <= 15:
            raise ValueError("字符串长度不符")
        if not re.match(r"^[a-zA-Z0-9_]+$", value):  #Python 自带的正则表达式模块
            raise ValueError("不能带特殊字符")

        return value

    @field_validator("password")
    def checkPassWord(cls , value : str) -> str:

        if not len(value) >= 8:
            raise ValueError("密码长度不符")
        if not (re.search(r"[a-zA-Z]", value) and re.search(r"[0-9]", value)):
            raise ValueError("密码必须包含字母和数字")

        return value

    @field_validator("phone")
    def checkPhone(cls , value : str | None ) -> str | None :

        if value is None:
            return None

        if not len(value) == 11:
            raise ValueError("电话长度不对")

        if not re.match(r"^1\d{10}$", value):
            raise ValueError("手机号必须是11位数字，以1开头")

        return value

    @model_validator(mode="after")
    def checkRegisterDate(self) -> "CheckUser" :
        today = datetime.now().strftime("%Y-%m-%d")

        if self.register_date > today:
            raise ValueError("注册日期不能晚于今天")
        return self


if __name__ == "__main__" :
    result = CheckUser(username="47151",password="qwer4345",email="47151@qq.com",phone="13240810066")
    print(result.model_dump())



