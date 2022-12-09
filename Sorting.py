from Calculate import Caculate
from Calculate import OPERATOR_TIMES, OPERATOR_DEFICION, OPERATOR_ADD, OPERATOR_SUBTRACT
from Delete import Delete

som_plus = [1, '+', 2]
som_minus = [3, '-', 4]
som_times = [5, '*', 6]
som_deficion = [7, '/', 8]
som_plus_times = [9, '+', 10, '*', 5, '/', 5]
som_haakje = [11, 'x', '(', 2, '+', 3, ')']

Operatortimes1, Operatortimes2 = 'x', '*'
OperatorDeficion1, OperatorDeficion2 = '/', '\\'
HaakjeRight, HaakjeLeft = '(', ')'

class Sorting(Caculate):
    def Caculete(ClientInput: list) -> str:
        Times = ClientInput.count(Operatortimes1) + ClientInput.count(Operatortimes2)
        Deficion = ClientInput.count(OperatorDeficion1) + ClientInput.count(OperatorDeficion2)
        Add = ClientInput.count(OPERATOR_ADD)
        Subtract = ClientInput.count(OPERATOR_SUBTRACT)	

        for _ in range(Times+Deficion):
            if Times >= 1 and Deficion >= 1:
                if ClientInput.index(OPERATOR_TIMES) > ClientInput.index(OPERATOR_DEFICION): 
                    Caculate.Deficion(ClientInput); Deficion -=1
                else:
                    Caculate.Times(ClientInput); Times -= 1
            if Deficion >= 1 and Times < 1:
                Caculate.Deficion(ClientInput); Deficion -= 1
            if Times >=1 and Deficion < 1:
                Caculate.Times(ClientInput); Times -= 1
        
        # add
        for _ in range(Add+Subtract):
            if Add >= 1 and Subtract >= 1:
                if ClientInput.index(OPERATOR_ADD) > ClientInput.index(OPERATOR_SUBTRACT): 
                    Caculate.Add(ClientInput); Add -=1
                else:
                    Caculate.Subtract(ClientInput); Subtract -= 1
            if Add >= 1 and Subtract < 1:
                Caculate.Add(ClientInput); Add -= 1
            if Subtract >=1 and Add < 1:
                Caculate.Subtract(ClientInput); Subtract -= 1
        return ClientInput[0]

    def Haakjes(ClientInput: list) -> list:
        Again = False
        if ClientInput.count(HaakjeRight) + ClientInput.count(HaakjeLeft) < 1:
            return None
        for _ in enumerate(ClientInput):
            Haakje1 =  ClientInput.index(HaakjeRight)
            if ClientInput.count(HaakjeRight) > 1:
                Haakje1 = ClientInput.index(Haakje1, HaakjeRight); Again = True
            else: break
        Haakje2 = ClientInput.index(HaakjeLeft)
        del ClientInput[Haakje1]
        del ClientInput[Haakje2-1]
        Anser = Sorting.Caculete(ClientInput[Haakje1:Haakje2])
        ClientInput = Delete(ClientInput, Anser, Haakje1+1)
        if Again is True:
            Sorting.Haakjes(ClientInput)
        return ClientInput[0]
