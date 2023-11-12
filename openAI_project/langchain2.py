from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("llama2.pdf")
pages = loader.load_and_split()

print(pages[0].page_content)

import re, wordninja

#预处理字符全都连在一起的行
def preprocess(text):
    def split(line):
        tokens = re.findall(r'\w+|[.,!?;%$-+=@#*/]', line)
        return [
            ' '.join(wordninja.split(token)) if token.isalnum() else token
            for token in tokens
        ]

    lines = text.split('\n')
    for i,line in enumerate(lines):
        if len(max(line.split(' '), key = len)) >= 20: 
            lines[i] = ' '.join(split(line))
    return ' '.join(lines)

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50,  # 思考：为什么要做overlap
    length_function=len,
    add_start_index=True,
)

paragraphs = text_splitter.create_documents([preprocess(pages[3].page_content)])
for para in paragraphs:
    print(para.page_content)
    print('-------')
    

from langchain.retrievers import TFIDFRetriever  # 最传统的关键字加权检索
from langchain.text_splitter import RecursiveCharacterTextSplitter
import wordninja, re

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=60,  
    length_function=len,
    add_start_index=True,
)

# 取一个有信息量的章节（Introduction: 第2-3页）
paragraphs = text_splitter.create_documents(
    [preprocess(d.page_content) for d in pages[2:4]]
)

user_query = "Does llama 2 have a dialogue version?"

retriever = TFIDFRetriever.from_documents(paragraphs)
docs = retriever.get_relevant_documents(user_query)

print(docs[0].page_content)

from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

template = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "你是问答机器人，你根据以下信息回答用户问题。\n" +
            "已知信息：\n{information}\n\nBe brief, and do not make up information."),
        HumanMessagePromptTemplate.from_template("{query}"),
    ]
)

llm = ChatOpenAI(temperature=0)
response = llm(
            template.format_messages(
                information=docs[0].page_content,
                query=user_query
            )
        )
print(response.content)