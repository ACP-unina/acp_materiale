from interface import Subject

## implementazione di Subject
class RealSubject(Subject): #realsubject implement subjet
    
    def request(self, data):
        # reverse the given string from client
        data = data[::-1]

        return data
