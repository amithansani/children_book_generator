from src.story_generation.book_details import BookDetails
from src.utils.llm_model import LLMModel
import json


class Storyline:
    def __init__(self, book:BookDetails):
        self.book=book

    # def generate_storyline(self):
    #     pass

    def _get_prompt(self):
        prompt=f"""
        You are a storyteller. You will be given a prompt and you will generate a storyline.
        Use the details of the book to generate a storyline.
        "Book Name": {self.book.name}
        "Age Group": {self.book.age_group}
        "Genre": {self.book.genre}
        "Characters": {self.book.characters}
        "Key Events": {self.book.key_events}
        "Instruction": {self.book.instruction}
        If any of the details are missing, do not use them, and make up your own details.
        Just generate a story line in 2-3 lines. This is not a detailed story.
        return the response in following json format
        {{
        
        "book_name":"Book Name",
        "Genre": "Genre",
        "characters":["Characters"],
        "key Events":["Key Events"],
        "storyline":"Storyline"
        
         }}
         All the keys should be in lowercase
        """
        return prompt

    def _get_response(self):
        prompt=self._get_prompt()
        model=LLMModel()
        response=model.groq_chat(prompt)
        return response

    def generate_storyline(self):
        response=self._get_response()
        response=json.loads(response)
        self.book.storyline=response["storyline"]


        return self.book





