import json

class Token:
    @staticmethod
    def getToken(path):
        with open(path, "r") as f:
            data = json.load(f)
        
        token = data["client"]["token"]
        return token;

class Icons:
    class Dev:
        python_logo = "<:pythonlogo:1434164317007253619>"
        disnake_logo = "<:disnakelogo:1434167456896913408>"
    
    class Server:
        white_frog = "<:whitefrog:1428126583276961853>"