from skeleton import Skeleton

class ServiceImpl(Skeleton): # ServiceImpl estende Skeleton che implementa ServiceInterface (il mio servizio)
    
    def inverti_stringa(self, data):
        # reverse the given string from client
        data = data[::-1]

        return data
