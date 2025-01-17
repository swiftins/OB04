# не используем принцип инверсии зависимостей
"""class Book():
    def read(self):
        print("Чтение интересной истории")
class StoryReader():
    def __init__(self):
        self.book = Book ()
    def tell_store(self):
        self.book.read()"""
from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Чтение интересной истории")

class AudioBook(StorySource):
    def get_story(self):
        print("Чтение интересной истории вслух")

class StoryReader:
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

# Create instances of Book and AudioBook
book = Book()
audioBook = AudioBook()

# Create StoryReader objects
readerBook = StoryReader(book)
readerAudioBook = StoryReader(audioBook)

# Use the tell_story method
readerBook.tell_story()  # Output: Чтение интересной истории
readerAudioBook.tell_story()  # Output: Чтение интересной истории вслух




    
