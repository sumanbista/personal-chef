from langchain.messages import HumanMessage

from src.agents.chef_agent import build_chef_agent


def test_agent_memory():
    agent = build_chef_agent()

    config = {
        "configurable": {
            "thread_id": "memory-test"
        }
    }

    agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="My favorite ingredient is chicken."
                )
            ]
        },
        config,
    )

    response = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="What is my favorite ingredient?"
                )
            ]
        },
        config,
    )

    answer = response["messages"][-1].content

    assert answer is not None
    assert "chicken" in answer.lower()