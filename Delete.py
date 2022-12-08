OPERATOR = '/', '\\', '+', '-', 'x', '*'

def Delete(ClientInput: list, Anser: str, DeletePlace: int) -> list:
    for i in range(3): 
        del ClientInput[DeletePlace-1]

    if DeletePlace <= 1: 
        ClientInput.insert(0, Anser)
        print(ClientInput, Anser, DeletePlace, 'test1a')
        return ClientInput

    if len(ClientInput) < DeletePlace:
        ClientInput.insert(len(ClientInput), Anser)
        return ClientInput

    for place, txt in enumerate(ClientInput):
        if txt in OPERATOR and ClientInput[place-1] in OPERATOR:
            ClientInput.insert(place, Anser)
            print(ClientInput, Anser, DeletePlace, 'test1b')
            break
    return ClientInput

