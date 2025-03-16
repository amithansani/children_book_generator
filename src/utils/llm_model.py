import ollama
import subprocess
from src.configs.model_configs import MODEL
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

class LLMModel:
    def __init__(self):
        self.model = MODEL


    def ollama_chat(self, prompt):
        response=ollama.chat(model=self.model,messages=[{'role':'assistant','content':prompt}])
        return response['message']['content']



    load_dotenv()
    def groq_chat(self,prompt):
        GroqModel = ChatGroq(model="llama-3.3-70b-versatile")
        response = GroqModel.predict(prompt)
        return response


