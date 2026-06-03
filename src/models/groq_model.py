from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_model():
    return ChatGroq(
        model="qwen/qwen3-32b",
        temperature = 0.2,
        max_tokens= 1024,
        timeout=None,
        max_retries=2
    )
