
class Calculator:
    def __init__(self):
        self.__total = 0
    
    def _addition(self, inputOne, inputTwo):
        self.__total = inputOne + inputTwo
        print(self.__total)
        return self.__total
    
    def _subtraction(self, inputOne, inputTwo):
        self.__total = inputOne - inputTwo
        print(self.__total)
        return self.__total
    
    def _multiply(self, inputOne, inputTwo):
        self.__total = inputOne * inputTwo
        print(self.__total)
        return self.__total

    def _divide(self, inputOne, inputTwo):
        self.__total = inputOne / inputTwo
        print(self.__total)
        return self.__total

new_calculator = Calculator()

new_calculator._addition(1, 2)
new_calculator._subtraction(3, 1)
new_calculator._multiply(2, 3)
new_calculator._divide(10, 4)