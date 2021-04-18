"""
Only one instance of a class is allowed and it is public so that 
other classes can share it

Use cases - 
1. DB Connection
2. Configuration files
3. Loggers

Fun fact - 
Python's import statment returns modules that are singleton
"""

class Singleton:

    __shared_instance = 'PP'

    @staticmethod
    def get_instance():
        if Singleton.__shared_instance == 'PP':
            Singleton()
        return Singleton.__shared_instance


    def __init__(self):
        if Singleton.__shared_instance != 'PP':
            raise Exception("Can't change value. It's Singleton")
        else:
            Singleton.__shared_instance = self


if __name__ == "__main__":
  
    obj = Singleton()
    print(obj)
   
    obj = Singleton.get_instance()
    print(obj)
