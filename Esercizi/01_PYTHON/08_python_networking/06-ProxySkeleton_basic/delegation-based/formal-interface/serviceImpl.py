from interface import ServiceInterface

## implementazione di ServiceInterface
class ServiceImpl(ServiceInterface): #ServiceImpl implement subjet
    
    def inverti_stringa(self, data):
        # reverse the given string from client
        data = data[::-1]

        return data
