from UserInput import UserInput
from Sorting import Sorting

ClientInput = UserInput.UserInput() 
CheckHaakjes = Sorting.Haakjes(ClientInput)
if CheckHaakjes is None:
    print('No haakjes')
