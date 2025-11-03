import json
import time

class Token:
    @staticmethod
    def getToken(path):
        with open(path, "r") as f:
            data = json.load(f)
        
        token = data["client"]["token"]
        return token

class Icons:
    class Dev:
        python_logo = "<:pythonlogo:1434164317007253619>"
        disnake_logo = "<:disnakelogo:1434167456896913408>"
        
        # Boats
        boat_red = "<:redboat:1434273504643125380>"
        boat_yellow = "<:yellowboat:1434273501975416983>"
        boat_green = "<:greenboat:1434273503154143292>"
    
    class Server:
        white_frog = "<:whitefrog:1428126583276961853>"

import time
import threading

class UpTime:
	days = 0
	hours = 0
	minutes = 0
	seconds = 0
	uptime = ""

	@staticmethod
	def getUpTime():
		return UpTime.uptime

	@staticmethod
	def startCounting():
		while True:
			time.sleep(1)
			UpTime.seconds += 1
			if UpTime.seconds == 60:
				UpTime.seconds = 0
				UpTime.minutes += 1
				if UpTime.minutes == 60:
					UpTime.minutes = 0
					UpTime.hours += 1
					if UpTime.hours == 24:
						UpTime.hours = 0
						UpTime.days += 1
			UpTime.uptime = f"`{UpTime.days}`d `{UpTime.hours}`h `{UpTime.minutes}`m `{UpTime.seconds}`s"