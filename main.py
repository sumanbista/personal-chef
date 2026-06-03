from langchain.messages import HumanMessage
from src.agents.chef_agent import build_chef_agent


agent = build_chef_agent()

response = agent.invoke(
    {"messages":[HumanMessage(content="I have chicekn, rice, onions, and eggs. Find me a recipe from the web")]}
)

print(response["messages"][-1].content)