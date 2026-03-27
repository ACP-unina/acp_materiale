from serviceSkeleton import ServiceSkeleton

# Service Implementation
class ServiceImpl(ServiceSkeleton):
    
    def deposita(self, data):

        self.queue.put(data)
        print("[SERVER-IMPL] Depositato", data)
        
        return "Depositato"
    
    def preleva(self):

        result = self.queue.get()
        print("[SERVER-IMPL] Prelevato", result)
        
        return result
