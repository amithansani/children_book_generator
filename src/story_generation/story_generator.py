from src.story_generation.book_details import BookDetails
from src.utils.llm_model import LLMModel
import ast

import json

class StoryGenerator:
    def __init__(self,book:BookDetails):
        self.book=book

    def _get_prompt(self):


        prompt=f"""
        You are writing a book for children.
        Use the storyline: {self.book.storyline}
        Use the details of the book to write the book.
        Write book with page limit {self.book.page_limit}
        Each page should have limit of {self.book.text_limit_each_page} words, with minimum of 10 words
        The book should have characters {self.book.characters}. But you can add more characters.
        The book should have key events {self.book.key_events}. BUt you can add more key events.
        Follow the genre of book as {self.book.genre}
        
        Respond the book in the following json format
        {{
        "number_of_pages":"number",
        "characters":["updated characters"],
        "key_events":["updated key events"],
        "pages":[
        {{"page1":"story of page 1"}},
        {{"page2":"story of page 2"}}
        ]
        }}
        
        """
        return prompt
        
    def _get_response(self):
        prompt=self._get_prompt()
        model=LLMModel()
        response=model.groq_chat(prompt)
        return response

    def generate_story(self):
        response=self._get_response()
        response=json.loads(response)
        self.book.num_of_pages=int(response["number_of_pages"])
        self.book.pages=response["pages"]
        self.book.characters=response["characters"]
        self.book.key_events=response["key_events"]

        print(response)
        return self.book
