from src.story_generation.book_details import BookDetails
from src.story_generation.storyline import Storyline
from src.story_generation.story_generator import StoryGenerator
from src.story_generation.character_descriptor import CharacterDescriptor
print("Welcome to the Children Book Generator!")

name = "The Little Prince"
age_group = "3-5"
page_limit = 10
text_limit_each_page=30
genre="Fantasy"
characters=["Prince","Princess","Prince's Parents"]
key_events=["Prince's Adventure"]
instruction="Need story of a prince and princess going on an adventure"
storyline=""
number_of_pages=0
pages=[]

book=BookDetails(name,age_group,page_limit,text_limit_each_page,genre,characters,key_events,instruction,storyline,number_of_pages,pages)
updated_book=Storyline(book).generate_storyline()
updated_book=StoryGenerator(updated_book).generate_story()
CharacterDescriptor(updated_book).describe_characters()

# print(updated_book)


