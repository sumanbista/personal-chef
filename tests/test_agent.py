from src.agents.chef_agent import build_chef_agent
from langchain.messages import HumanMessage

def test_build_chef_agent():
    agent = build_chef_agent()

    config = {
        "configurable": {
            "thread_id": "test-thread"
        }
    }


    response = agent.invoke(
        {
            "messages":[
                HumanMessage(
                    content="I have rice and chicken."
                )
            ]
        },
        config,
    )

    assert response is not None
    assert "messages" in response
    assert len(response["messages"]) > 0
