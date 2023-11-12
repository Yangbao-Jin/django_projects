from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate

#例子(few-shot)
examples = [
    {
        "input": "北京天气怎么样",
        "output" : "北京市"
    },
    {
        "input": "南京下雨吗",
        "output" : "南京市"
    },
    {
        "input": "江城热吗",
        "output" : "武汉市"
    }
]

#例子拼装的格式
example_prompt = PromptTemplate(input_variables=["input", "output"], template="Input: {input}\nOutput: {output}")

#Prompt模板
prompt = FewShotPromptTemplate(
    examples=examples, 
    example_prompt=example_prompt, 
    suffix="Input: {input}\nOutput:", 
    input_variables=["input"]
)

prompt = prompt.format(input="羊城多少度")

print("===Prompt===")
print(prompt)

llm = OpenAI()
response = llm(prompt)

print("===Response===")
print(response)