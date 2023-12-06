import json

class Config:
    def __init__(self):

        try:
            self.configFile = open('config.json', 'r')
            self.configData = json.load(self.configFile)

            if len(self.configData['user']):
                self.userName = self.configData['user']

            if len(self.configData['password']):
                self.userPassword = self.configData['password']

            if len(self.configData['appPath']):
                self.appPath = self.configData['appPath']

            self.configFile.close()
        except:
            #jeśli wyjątek w braku json'a inicjalizuj pusty :)
            pass


    def __str__(self):
        return f"Użytkownik: { self.userName }\n" \
               f"Hasło: { self.userPassword }\n" \
               f"Ścieżka do aplikacji: { self.appPath }\n "