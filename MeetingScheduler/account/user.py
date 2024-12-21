class User: 
    def __init__(self, password: str, userId: str): 
        self._password = password
        self._userId = userId
        self._isAdmin = False
        self._inbox = []

    def isAdmin(self): 
        return self._isAdmin
    
    def getMail(self, message: str):
        self._inbox.append(message) 

    def getUserId(self) -> str: 
        return self._userId