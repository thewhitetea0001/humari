import disnake
from utilities.log import Log
from disnake.ext import commands

class OnSlashCommandError(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, error):
		user = getattr(error, "argument", "uknow")
		if isinstance(error, commands.MemberNotFound):
			Log.warn("scmd", inter.data.name, f"({inter.author.name}) Could not found user with ID '{user}'")
			await inter.response.send_message(f"Не удалось найти пользователя с ID `{user}`", ephemeral=True)
		else:
			Log.error("scmd", inter.data.name, error)
        

		if isinstance(error, commands.CommandOnCooldown):
			await inter.response.send_message(f"Пожалуйста, подождите {error.retry_after:.1f} сек. ({int(error.retry_after/60)} мин.)", ephemeral=True)
			Log.warn("scmd", inter.data.name, f"({inter.author}) The user has exceeded command usage limit")
		else:
			Log.error("scmd", inter.data.name, f"({inter.author}) {error}")

def setup(client):
	client.add_cog(OnSlashCommandError(client))