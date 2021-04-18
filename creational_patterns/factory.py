"""
Just like a factory, this pattern is used to create objects of different types

Imagine a translation service. You don't want to change code if you have to add
new language. At max, you just have to add a class for that language and then at
the time of object creation, simply mention the language

Use cases - 
Any case where updating/adding new feature might result in a shit ton of work.
"""

class SpanishLocalizer:


    def __init__(self):
        self.translations = {
            'car': 'car in spanish',
            'bike': 'bike in spanish',
            'cycle': 'cycle in spanish'
        }

    
    def localize(self, message):
        return self.translations.get(message, message)


class FrenchLocalizer:


    def __init__(self):
        self.translations = {
            'car': 'car in french',
            'bike': 'bike in french',
            'cycle': 'cycle in french'
        }

    
    def localize(self, message):
        return self.translations.get(message, message)


class ItalianLocalizer:


    def __init__(self):
        self.translations = {
            'car': 'car in italian',
            'bike': 'bike in italian',
            'cycle': 'cycle in italian'
        }

    
    def localize(self, message):
        return self.translations.get(message, message)


def localizer_factory(language):
    localizers = {
        'Spanish': SpanishLocalizer,
        'French': FrenchLocalizer,
        'Italian': ItalianLocalizer,
    }
    return localizers[language]()


if __name__ == '__main__':
    s = localizer_factory('Spanish')
    f = localizer_factory('French')
    i = localizer_factory('Italian')

    messages = ['car', 'bike', 'cycle']

    for msg in messages:
        print(f"{msg} in Spanish - {s.localize(msg)}")
        print(f"{msg} in French - {f.localize(msg)}")
        print(f"{msg} in Italian - {i.localize(msg)}")
        print('-' * 20)