# 加载环境变量
import openai
import os
import json

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # 读取本地 .env 文件，里面定义了 OPENAI_API_KEY

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # 模型输出的随机性，0 表示随机性最小
        functions=[{  # 用 JSON 描述函数。可以定义多个，但是只有一个会被调用，也可能都不会被调用
            "name": "sum",
            "description": "计算一组数的加和",  
            "parameters": {
                "type": "object",
                "properties": {
                    "numbers": {
                        "type": "array",
                        "items": {
                            "type": "number"
                        }
                    }   
                }
            },
        }],
    )
    return response.choices[0].message


from math import *

# prompt = "Tell me the sum of 1, 2, 3, 4, 5, 6, 7, 8, 9, 10."
# prompt = "桌上有 2 个苹果，四个桃子和 3 本书，一共有几个水果？"
prompt = "1+2+3...+99+100"

messages = [
    {"role": "system", "content": "你是一个小学数学老师，你要教学生加法"},
    {"role": "user", "content": prompt}
]
response = get_completion(messages)
messages.append(response)  # 把大模型的回复加入到对话中
print("=====GPT回复=====")  
print(response)

# 如果返回的是函数调用结果，则打印出来
if (response.get("function_call")): 
    # 是否要调用 sum
    if (response["function_call"]["name"] == "sum"):
        args = json.loads(response["function_call"]["arguments"])
        result = sum(args["numbers"])
        print("=====函数返回=====")
        print(result)
        messages.append(
            {"role": "function", "name": "sum",
                "content": str(result)}  # 数值result 必须转成字符串
        )
        print("=====最终回复=====")
        print(get_completion(messages).content)
        