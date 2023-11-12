from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="为生产{product}的公司取一个亮眼中文名字：",
)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("ACSL Guide"))
