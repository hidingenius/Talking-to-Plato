import gradio as gr
from ollama import Client

MODEL = "llama3.2:3b"          # small & fast (~2–3 GB) — change to llama3.1:8b etc. if desired
client = Client()              # assumes Ollama is running locally

# Load system prompt
with open("plato_prompt.txt", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

def plato_chat(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        if assistant_msg:
            messages.append({"role": "assistant", "content": assistant_msg})
    
    messages.append({"role": "user", "content": message})
    
    response = ""
    stream = client.chat(
        model=MODEL,
        messages=messages,
        stream=True,
    )
    
    for chunk in stream:
        content = chunk['message']['content']
        response += content
        yield response

demo = gr.ChatInterface(
    fn=plato_chat,
    title="Dialogue with a Student of Plato",
    description=(
        "Speak with a humble follower of Socrates & Plato. "
        "Expect many questions, few answers — the goal is your own thinking."
    ),
    examples=[
        "What is justice?",
        "Is democracy the best form of government?",
        "Why do people desire beauty?",
        "What is the nature of knowledge?",
    ],
    cache_examples=False,
)

if __name__ == "__main__":
    demo.launch()
