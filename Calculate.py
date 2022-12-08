TIMES = lambda x, y: x * y
from Delete import Delete
OPERATOR_TIMES = '*' or 'x'
OPERATOR_DEFICION = '/'or '\\'
OPERATOR_ADD = '+'
OPERATOR_SUBTRACT = '-'

DEFICION = lambda x, y: x/y
ADD = lambda x, y: x + y	
SUBTRACT = lambda x, y: x-y


class Caculate:
    def Times(UserInput: list) -> list:
        Operator = UserInput.index(OPERATOR_TIMES)  
        Answer = TIMES(UserInput[Operator-1], UserInput[Operator+1])
        return Delete(UserInput, Answer, Operator)

    def Deficion(UserInput: list) -> list:
        Operator = UserInput.index(OPERATOR_DEFICION)
        Answer = DEFICION(UserInput[Operator-1], UserInput[Operator+1])
        return Delete(UserInput, Answer, Operator)
    
    def Add(UserInput: list) -> list:
        Operator = UserInput.index(OPERATOR_ADD)
        Answer = ADD(UserInput[Operator-1], UserInput[Operator+1])
        return Delete(UserInput, Answer, Operator)

    def Subtract(UserInput: list) -> list:
        Operator = UserInput.index(OPERATOR_SUBTRACT)
        Answer = SUBTRACT(UserInput[Operator-1], UserInput[Operator+1])
        return Delete(UserInput, Answer, Operator)
    