from dataclasses import dataclass
@dataclass
class BookDetails:
    name:str
    age_group:str
    page_limit:int
    text_limit_each_page:int
    genre:str
    characters:list
    key_events:list
    instruction:str
    storyline:str
    num_of_pages:int
    pages:list



