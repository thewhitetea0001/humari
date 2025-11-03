import disnake
from utilities.log import Log
from disnake.ext import commands

class OnReady(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		Log.info("scmd", "on_ready", f"Client logged as: {self.client.user}")

def setup(client):
	client.add_cog(OnReady(client))