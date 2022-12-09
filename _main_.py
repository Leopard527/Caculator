from UserInput import UserInput
from Sorting import Sorting

ClientInput = UserInput.UserInput() 
CheckHaakjes = Sorting.Haakjes(ClientInput)
if CheckHaakjes is not None:
    Anser = Sorting.Haakjes(ClientInput)
if len(Anser) > 1:
    print('Caculated')
Sorting.Caculete(Anser)
print('Caculated')
print(Anser)


