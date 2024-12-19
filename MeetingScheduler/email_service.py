from account.user import User

class EmailService: 
    def sendEmailToUser(self, user: User, mail: str): 
        user.getMail(message = mail)