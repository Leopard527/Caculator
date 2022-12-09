from Calculate import OPERATOR_TIMES, OPERATOR_DEFICION, OPERATOR_ADD, OPERATOR_SUBTRACT
from string import digits

StringReplaeInt = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
class UserInput:
    def UserInput() -> list:
        ClientInput = input('Please enter youre som: ')
        while ClientInput not in (digits) and ClientInput in ('+-()*x/\\'):
            ClientInput = input('Please enter youre som: ')
        ClientInput = list(ClientInput)
        #Credits https://stackoverflow.com/users/8747/rob%e1%b5%a9
        [StringReplaeInt.get(item, item) for item in ClientInput]
        return ClientInput


        