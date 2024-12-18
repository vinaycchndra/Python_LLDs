class User: 
    def __init__(self, password: str, userId: str): 
        self._password = password
        self._userId = userId
        self._isAdmin = False

    def isAdmin(self): 
        return self._isAdmin