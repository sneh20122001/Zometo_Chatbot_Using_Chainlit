# import chainlit as cl
# from src.llm import ask_order, messages

# @cl.on_message
# async def main(message: cl.Message):
#     # Your custom logic goes here...
#     messages.append({"role": "user", "content": message.content})
#     response = ask_order(messages)
#     messages.append({"role": "assistant", "content": response})

#     # Send a response back to the user
#     await cl.Message(
#         content=response,
#     ).send()


import chainlit as cl
from src.llm import ask_order, messages

@cl.on_message
async def main(message: cl.Message):
    # Check if user's name is already stored
    user_name = cl.user_session.get("name")

    if not user_name:
        # Save the user's name
        cl.user_session.set("name", message.content)
        user_name = message.content

        # Greet the user
        await cl.Message(
            content=f"# Welcome {user_name}\n, how can I assist you with your order?"
        ).send()
        return

    # Regular LLM message handling
    messages.append({"role": "user", "content": message.content})
    response = ask_order(messages)
    messages.append({"role": "assistant", "content": response})

    await cl.Message(content=response).send()

@cl.on_chat_start
async def start():
    await cl.Message(
        content="# Welcome to Zometo Bot!\nHi there! What's your name?"
    ).send()
