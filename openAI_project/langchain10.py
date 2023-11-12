from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("llama2.pdf")
pages = loader.load_and_split()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, 
    chunk_overlap=60,
    length_function=len,
    add_start_index=True,
)

texts = text_splitter.create_documents([pages[2].page_content,pages[3].page_content])

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0), #语言模型
    chain_type="stuff",  # prompt的组织方式，后面细讲
    retriever=db.as_retriever() # 检索器
)
query = "llama 2能商用吗"
response = qa_chain.run(query)
print(response)

print('================qa_chain===============')
print(qa_chain)
print('======combine_documents_chain==========')
print(qa_chain.combine_documents_chain.document_prompt)
print('==============llm_chain================')
print(qa_chain.combine_documents_chain.llm_chain.prompt.template)

