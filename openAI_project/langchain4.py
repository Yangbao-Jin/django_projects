from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings() # 默认是text-embedding-ada-002
text = "这是一个测试"
document = "测试文档"
query_vec = embeddings.embed_query(text)
doc_vec = embeddings.embed_documents([document])

print(len(query_vec))
print(query_vec[:10])  # 为了展示方便，只打印前10维
print(len(doc_vec[0]))
print(doc_vec[0][:10])  # 为了展示方便，只打印前10维

