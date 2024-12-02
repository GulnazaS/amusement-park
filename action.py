class Action:
    def __init__(self, name: str, duration: int, min_age: int, max_age: int):
        self.__name = name
        self.__duration = duration
        self.__min_age = min_age
        self.__max_age = max_age
 
    @property
    def name(self):
        return self.__name
 
    @property
    def duration(self):
        return self.__duration
    
    @property
    def min_age(self):
        return self.__min_age

    @property
    def max_age(self):
        return self.__max_age
 
    def __str__(self):
       return self.name
   
    def run(self):
        raise NotImplementedError
