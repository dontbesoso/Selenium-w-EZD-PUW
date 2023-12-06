
from User import User
from Config import Config

class App:

    config = Config()
    user = User()

    def __init__(self):
        self.path = self.config.appPath
        self.user.name = self.config.userName
        self.user.password = self.config.userPassword

        self.VIEWSTATE = "%2FwEPDwULLTEzNzIzMTI2NjZkZJMDbwnwUTO%2F6TZtQlLgscvelkyA"
        self.VIEWSTATEGENERATOR = "5A2128B1"
        self.EVENTVALIDATION = "%2FwEdAAXrk1sShrnntt54q5w5nD6GCRuj612N3iFOLmAHpOgVJsXJ%2BqCA3WzUCOQEFCCMr%2BJ2NvjHOkq5wKoqN6Aim8WGRaUwvhOTLLHHbglAIUbi%2B4jccx%2F0GULCOj25iy1IOXwKMljy&hdnLoginPbi="

    def getAuthPath(self):
        return f"{ self.path }/logon.aspx?__VIEWSTATE={ self.VIEWSTATE }&__VIEWSTATEGENERATOR={ self.VIEWSTATEGENERATOR }&__EVENTVALIDATION={ self.EVENTVALIDATION }&hdnLoginPbi=&txtLogin={ self.user.name }&txtPassword={ self.user.password }&btnLogon=Loguj"
        pass