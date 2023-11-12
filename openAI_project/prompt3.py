import openai
import os


from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

messages = [
    {
        "role": "system",
        "content": "你是AI助手小瓜.你是AGIClass的助教。这门课每周二、四上课。"
    },
    {
        "role": "user",
        "content": "你是干什么的?什么时间上课"
    },

]

# 调用ChatGPT-3.5
chat_completion = openai.ChatCompletion.create(
    model="gpt-4", messages=messages)

# 输出回复
print(chat_completion.choices[0].message.content)