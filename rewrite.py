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
    "FPS": "帧每秒",

    # 其他单位
    "+": "加",
}

ignore_dict = [
    r"[12]\d{3}\s*[年款]",
    r"\d+%"
]

replace_dict = {
    "+": "加"
}


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
    # replace characters in replace_dict
    for k, v in replace_dict.items():
        text = text.replace(k, v)

    regex_from_to = r'(\d+)\s*-\s*(\d+)'
    text = re.sub(regex_from_to, r'\1至\2', text)

    regex_num_unit = r"(\d+\.?\d*)\s*([A-Za-z/°²³%\+]+|[\u4e00-\u9fa5])"
    result = []

    last_end = 0
    for match in re.finditer(regex_num_unit, text):
        number = match.group(1)
        unit = match.group(2)

        match_str = number + unit
        print(match_str)
        if any(re.match(regex, match_str) for regex in ignore_dict):
            continue

        # transform number to chinese
        chinese_number = number_to_chinese(number)
        # transform unit to chinese
        unit = unit_dict.get(unit.upper(), unit)

        # append chinese number and unit to result list
        result.append(text[last_end:match.start()] + chinese_number + unit)

        # update last position
        last_end = match.end()

    # add the rest of the text to result list
    result.append(text[last_end:])

    return ''.join(result)


if __name__ == '__main__':
    test_text = "鹿客2024款智能锁P7Pro，2023-2024范围，市占率99%，拥有142°超广角智能猫眼，1080P高清摄像头+纳米红外光夜视，500mah电池"
    print(transcribe(test_text))
