from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory

history = ConversationBufferMemory()
history.save_context({"input": "你好啊"}, {"output": "你也好啊"})

print(history.load_memory_variables({}))

history.save_context({"input": "你再好啊"}, {"output": "你又好啊"})

print(history.load_memory_variables({}))

from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()

history.add_user_message("你好!")

history.add_ai_message("有什么可以帮您?")

print(history)

from langchain.memory import ConversationBufferWindowMemory

window = ConversationBufferWindowMemory(k=2)
window.save_context({"input": "第一轮问"}, {"output": "第一轮答"})
window.save_context({"input": "第二轮问"}, {"output": "第二轮答"})
window.save_context({"input": "第三轮问"}, {"output": "第三轮答"})
print(window.load_memory_variables({}))

from langchain.memory import ConversationSummaryMemory
from langchain.llms import OpenAI

memory = ConversationSummaryMemory(
    llm=OpenAI(temperature=0),
    # buffer="The conversation is between a customer and a sales."
    buffer="以中文表示"
)
memory.save_context(
    {"input": "你好"}, {"output": "你好，我是你的AI助手。我能为你回答有关AGIClass的各种问题。"})

print(memory.load_memory_variables({}))