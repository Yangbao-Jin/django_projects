import openai
import os


openai.api_key = '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'

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # 模型输出的随机性，0 表示随机性最小
    )
    return response.choices[0].message["content"]


instructions = """
求递归函数的值
"""
# 用户输入
input_text = """
Problem: Find the value of h(13) given the following definition of h:

h(x)={h(x−7)+1  when x>5
x   when 0≤x≤5
h(x+3) when x<0

"""
prompt=f"""
{instructions} 

用户输入：{input_text}
"""
response = get_completion(prompt)
print(response)
