from langchain_google_genai import ChatGoogleGenerativeAI
from src.prompt import system_instruction 
from dotenv import load_dotenv
import os 
load_dotenv() 


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature = 0.7
)

messages = [
    {"role":"system","content":system_instruction}
]

def ask_order(messages):

    response = llm.invoke(messages)

    return response.content
# from langchain.schema.messages import SystemMessage, HumanMessage


# # Function to ask a question
# def ask_order(messages):
#     # Convert raw messages into LangChain-compatible messages
#     lc_messages = []
#     for msg in messages:
#         if msg["role"] == "system":
#             lc_messages.append(SystemMessage(content=msg["content"]))
#         elif msg["role"] == "user":
#             lc_messages.append(HumanMessage(content=msg["content"]))
#         else:
#             raise ValueError(f"Unsupported message role: {msg['role']}")

#     # Call the model
#     response = llm.invoke(lc_messages)
#     return response.content

