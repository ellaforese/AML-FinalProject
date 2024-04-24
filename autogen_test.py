import os
from autogen import AssistantAgent, UserProxyAgent

# autogen also lets us alter the temperature
# note -- the way this code works (i think) saves previous conversation information 

llm_config = {"model": "gpt-4", "temperature": 0.9, "api_key": "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"}
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)





# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Write me a simple to-do list for a student preparing for school",
)