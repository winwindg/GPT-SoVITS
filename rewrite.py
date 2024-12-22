import re

import cn2an

unit_dict = {
    # 长度单位
    "M": "米",
    "NM": "纳米",
    "UM": "微米",
    "MM": "毫米",
    "CM": "厘米",
    "DM": "分米",
    "KM": "千米",

    # 重量单位
    "G": "克",
    "KG": "千克",

    # 面积单位
    "MM²": "平方毫米",
    "CM²": "平方厘米",
    "M²": "平方米",
    "KM²": "平方千米",

    # 体积单位
    "MM³": "立方毫米",
    "CM³": "立方厘米",
    "M³": "立方米",
    "ML": "毫升",

    # 温度单位
    "°C": "摄氏度",
    "°F": "华氏度",
    "°": "度",

    # 电力单位
    "MAH": "毫安时",
    "W": "瓦",
    "KW": "千瓦",

    # 速度单位
    "KM/H": "千米每小时",
    "M/S": "米每秒",
    "MPH": "英里每小时",

    # 频率单位
    "HZ": "赫兹",
    "KHZ": "千赫兹",
    "MHZ": "兆赫兹",
    "GHZ": "吉赫兹",

    # 时间单位
    "MS": "毫秒",

    # 计算机相关单位
    "FPS": "帧每秒"
}

regex_dict = [
    r"\d{4}\s*[年款]",
    r"\d+%"
]


def number_to_chinese(number: str):
    chinese_str = cn2an.an2cn(number)
    if len(number) >= 3 and chinese_str.startswith("二"):
        chinese_str = "两" + chinese_str[1:]
    return chinese_str


def year_to_chinese(year: str):
    chinese_year = ""
    for i in range(len(year)):
        chinese_year += number_to_chinese(year[i])
    return chinese_year


def transcribe(text):
    regex_num_unit = r"(\d+\.?\d*)\s*([A-Za-z/°²³%\+]+|[\u4e00-\u9fa5])"
    result = []

    last_end = 0
    for match in re.finditer(regex_num_unit, text):
        number = match.group(1)
        unit = match.group(2)

        match_str = number + unit
        if any(re.match(regex, match_str) for regex in regex_dict):
            continue

        # 将数字转为中文
        chinese_number = number_to_chinese(number)
        # 将单位转为中文
        unit = unit_dict.get(unit.upper(), unit)

        # 添加文本中的替换部分
        result.append(text[last_end:match.start()] + chinese_number + unit)

        # 更新上一个匹配的结束位置
        last_end = match.end()

    # 添加匹配后的文本后面部分（如果有的话）
    result.append(text[last_end:])

    # 返回替换后的完整文本
    return ''.join(result)
