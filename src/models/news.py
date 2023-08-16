import re
from dataclasses import dataclass

@dataclass
class News:
    title: str
    date: str
    description: str
    has_money: bool
    search_phrase_count: int
    image: [str|None]

    def __init__(self, title, date, description, search_phrase, image) -> None:
        self.title = title
        self.date = date
        self.description = description
        self.image = image
        self.has_money= self.has_money_in_title_or_description()
        self.search_phrase_count = self.count_search_phrases_in_title_and_description(search_phrase)
    
    def has_money_in_title_or_description(self):
        """Returns true if title or description contains money-related words"""
        pattern =  r'\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)|\b(\d+)\s*(?:dollars|USD)\b'
        search = re.search(pattern, self.title) or re.search(pattern, self.description)
        return search is not None
    
    def count_search_phrases_in_title_and_description(self, search_phrase):
        return (self.title.count(search_phrase) if self.title else 0) + (self.description.count(search_phrase) if self.description else 0)
