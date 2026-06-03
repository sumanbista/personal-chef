from src.models.groq_model import get_model
from src.prompts.chef_prompt import chef_prompt
from src.tools.web_search import web_search

from langchain.agents import create_agent

def build_chef_agent():
    model=get_model()
    
    return create_agent(
        model=model,
        system_prompt=chef_prompt,
        tools=[web_search],
    )