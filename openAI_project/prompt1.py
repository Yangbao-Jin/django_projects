import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = "今天我很"
response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=100,
    temperature=0,
    stream=True
)

for chunk in response:
    print(chunk.choices[0].text, end='')