from src.story_generation.book_details import BookDetails
from src.utils.llm_model import LLMModel

class CharacterDescriptor:
    def __init__(self,book:BookDetails):
        self.book=book

    def _get_prompt(self,character):
        prompt=f"""
        You are expert in designing detailed characters.
        You will be given a character and you will generate a detailed description of the character as the story of the book.
        Use the details of the book to generate a description of the character.
        
        
        "Key Events": {self.book.key_events}
        "pages": {self.book.pages}
        "storyline": {self.book.storyline}
        
        Provide description of the character so that image models can generate an image of the character.
        
        "character": {character}
        
        respond in text.  
        
        
        """

    def _get_response(self,prompt):

        model=LLMModel()
        response=model.groq_chat(prompt)
        return response

    def describe_characters(self):
        for character in self.book.characters:
            prompt_character=self._get_prompt(character)
            response=self._get_response(prompt_character)
            print(response)

