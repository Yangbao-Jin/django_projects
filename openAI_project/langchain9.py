
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from datetime import datetime

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.memory import VectorStoreRetrieverMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
import faiss

from langchain.docstore import InMemoryDocstore
from langchain.vectorstores import FAISS
from langchain.chains import ConversationChain

embedding_size = 1536 # OpenAIEmbeddings的维度
index = faiss.IndexFlatL2(embedding_size)
embedding_fn = OpenAIEmbeddings().embed_query
vectorstore = FAISS(embedding_fn, index, InMemoryDocstore({}), {})

# 实际应用中k可以稍大一些，这里k=1演示方便
retriever = vectorstore.as_retriever(search_kwargs=dict(k=1))
memory = VectorStoreRetrieverMemory(retriever=retriever)

# 把记忆存在向量数据库中
memory.save_context({"input": "我喜欢看电影"}, {"output": "不错啊"})
memory.save_context({"input": "我喜欢踢足球"}, {"output": "下次一起啊"})
memory.save_context({"input": "我不喜欢喝咖啡"}, {"output": "ok"}) 

template = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("你是我的朋友。我们的聊天记录：\n{history}"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

chain = ConversationChain(llm=ChatOpenAI(),memory=memory,prompt=template,verbose=True)

print(chain.run("周末一起去做运动吧?"))