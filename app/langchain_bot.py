from transformers.pipelines import pipeline 
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

generator = pipeline("text-generation", model="gpt2", return_full_text=True)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def ask_bot(user_input: str) -> str:

    response = generator(user_input, max_length=50, num_return_sequences=1)

    memory.save_context({"input": user_input}, {"output": response[0]['generated_text'] if response and isinstance(response, list) and 'generated_text' in response[0] else ""})
    output_text = response[0]['generated_text'] if response and isinstance(response, list) and 'generated_text' in response[0] else ""


    return output_text.strip() 
