import warnings
import disnake
import sys, os
import asyncio
import thread
from disnake.ext import commands
from utilities.bot import UpTime
from utilities.bot import Token
from utilities.log import Log

filename = os.path.basename(__file__)
warnings.filterwarnings("ignore")

thread.Thread(target=UpTime.startCounting, daemon=True).start()

# Intents
intents = disnake.Intents.default()
intents.members = True
intents.guilds = True

# Bot object
client = commands.InteractionBot(
    intents=intents
)

# Cogs / events
client.load_extension("modules.events.on_ready")
Log.log(filename, "Loaded cog: modules.events.on_ready")
client.load_extension("modules.events.on_member_join")
Log.log(filename, "Loaded cog: modules.events.on_member_join")

# Cogs / slash commands
client.load_extension("modules.slash_commands.botinfo")
Log.log(filename, "Loaded cog: modules.slash_commands.botinfo")
client.load_extension("modules.slash_commands.patpat")
Log.log(filename, "Loaded cog: modules.slash_commands.patpat")
client.load_extension("modules.slash_commands.economy.work")
Log.log(filename, "Loaded cog: modules.slash_commands.economy.work")

# Cogs / error handlers
client.load_extension("modules.events.error_handlers.on_slash_command_error")
Log.log(filename, "Loaded cog: modules.events.error_handlers.on_slash_command_error")


client.run(Token.getToken("src/config.json"))