#!/usr/bin/python
# coding=utf-8
from dataclasses import Field

# 1. 导入核心类
from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime
from enum import Enum  # Python内置枚举

# 2. 定义数据模型：继承BaseModel   # 白话解释：我定义一个天气数据规则手册
class WeatherQuery(BaseModel) :
    city : str                     # city 必须传，而且只能是字符串
    date : str = "today"           # date 可以不传，不传就用默认值today
    unit : str = "celsius"

# 3. 使用模型：传入数据
res = WeatherQuery(city = "北京", date = "2026-04-23")   # 把数据丢进规则手册，Pydantic 自动检查

# 4. 读取数据（和对象一样用）
print(res.city)    # 输出：北京
print(res.date)    # 输出：2026-04-23

# 5. 转字典/JSON（Agent/API必备）  # 把标准化数据转成字典，给 Agent / 接口用
print(res.model_dump())  # 新标准：{'city': '北京', 'date': '2025-12-25', 'unit': 'celsius'}

# 自定义pydantic

# 方式 1：Field 内置校验（最简单，推荐）
class NewQuery(BaseModel):
    city : str = Field (
        min_length = 2,
        max_length = 10,
        description="city name like BeiJing"
    )
    date : str = Field(default="today" , description = "data format")

query = NewQuery(city="北京")
print(query)

# 方式 2：field_validator 字段级校验（自定义规则）
class NewQuery(BaseModel):
    city : str
    date : str

    # @field_validator是v2专属，v1用 @validator
    @field_validator("city")   # 告诉 Pydantic：我要给 city 字段写自定义校验
    def check_city(cls , value : str):   # cls: 固定第一个参数，代表 WeatherQuery 这个类，语法强制要求，不写直接报错
        clean_value = value.replace(" " , "")
        if not clean_value:
            raise ValueError("城市名称不能为空！")  # 抛自定义错误
        # 校验器必须返回值!!（返回清洗后的数据）；
        return clean_value

    @field_validator("date")
    def check_date(cls , value : str):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except:
            # 抛ValueError会被 Pydantic 捕获，转为标准错误。
            raise ValueError("日期格式错误！请输入：YYYY-MM-DD")

query = NewQuery(city="北 京   ", date="2026-04-29")
print(query)


# 方式 3：model_validator 模型级校验（多字段关联）
class Query3(BaseModel):

    city : str
    date : str

    @field_validator("date")
    def check_date(cls , value : str):
        datetime.strptime(value,"%Y-%m-%d")
        return value

    @model_validator(mode="after")  # 校验范围是整个模型:能拿到所有字段的值
    def check_date_no_past(self):
        today = datetime.now().strftime("%Y-%m-%d")

        if self.date > today:   # self = 已经校验完成的模型对象,直接用 self.字段名 拿到所有合法的字段值！
            raise ValueError("日期不能大于今天")

        if self.city == "test":
            raise ValueError("不能是测试城市")

        return self

query = Query3(city="te", date="2026-04-20")
print(query)

# 方式 4：枚举类型（Enum）：固定选项，杜绝乱输入

# 定义单位枚举：固定两个选项
class TempUnit(str, Enum):
    CELSIUS = "celsius"   # 摄氏度
    FAHRENHEIT = "fahrenheit" # 华氏度

class WeatherQuery(BaseModel):
    city: str
    date: str
    # 字段只能选枚举里的值！
    unit: TempUnit = TempUnit.CELSIUS

query = WeatherQuery(city="北京", date="2025-12-25", unit="celsius")

# 嵌套模型
# 子模型：天气详情
class WeatherDetail(BaseModel):
    temp : str
    status : str

# 父模型：整体天气响应
class CityWeather(BaseModel):
    city : str
    date : str
    detail : WeatherDetail # 嵌套子模型

res = CityWeather(city="北京" , date="2026-04-03" , detail = {"temp" : "25" , "status" : "1"})
print(res.model_dump()) #  把 Pydantic 模型对象 → 转换成 普通 Python 字典（dict）

# 动态默认值（default_factory）
# 避坑重点：不能直接用datetime.now()当默认值，要用default_factory：
class WeatherQuery(BaseModel):
    city: str
    # 动态默认值：每次创建模型，都取当前时间
    date: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

res = WeatherQuery(city="上海")
print(res)
