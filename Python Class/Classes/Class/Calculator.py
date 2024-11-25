
class Calculator:
    def __init__(self):
        self.__total = 0
    
    def addition(self, inputOne, inputTwo):
        self.__total = inputOne + inputTwo
        print(self.__total)
        return self.__total
    

Calculator().addition(1,2)