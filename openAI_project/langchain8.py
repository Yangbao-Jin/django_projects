from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

template = """你是聊天机器人小瓜，你可以和人类聊天。

{memory}
Human: {human_input}
AI:"""

prompt = PromptTemplate(
    input_variables=["memory", "human_input"], template=template
)

# memory = ConversationBufferMemory(memory_key="memory")

memory = ConversationSummaryMemory(
    llm=OpenAI(temperature=0), 
    buffer="以中文表示", 
    memory_key="memory"
)

llm_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=prompt,
    verbose=True,
    memory=memory,
)

print(llm_chain.run("你是谁？"))
print("---------------")
output = llm_chain.run("我刚才问了你什么，你是怎么回答的？")
print(output)