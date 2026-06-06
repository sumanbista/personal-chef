from langchain.messages import HumanMessage
from src.agents.chef_agent import build_chef_agent


agent = build_chef_agent()

config = {
    "configurable":{
        "thread_id":"chef-demo"
    }
}

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = agent.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        },
        config,
    )

    print("\nChef:", response["messages"][-1].content)