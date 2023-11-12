from openai import OpenAI
import os
import time
import json

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

#client=OpenAI()
#client.api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)
while True:
    run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id)
    if run.status == "completed":
        break
    
#time.sleep(10)   

messages = client.beta.threads.messages.list(thread_id=thread.id)
first_message_value = messages.data[0].content[0].text.value
#first_message_value = messages.data[0].content[0]
print(first_message_value)
'''
#print()
while not run.status == "completed":
   pass

while not run.status == "queued":
    pass'''