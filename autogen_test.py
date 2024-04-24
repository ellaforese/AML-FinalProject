import os
from autogen import AssistantAgent, UserProxyAgent

llm_config = {"model": "gemini-pro", "api_key": os.environ["API-KEY"]}
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)





# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Write me a simple to-do list for a student preparing for school",
)