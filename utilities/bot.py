import json

class Token:
    @staticmethod
    def getToken(path):
        with open(path, "r") as f:
            data = json.load(f)
        
        token = data["client"]["token"]
        return token;