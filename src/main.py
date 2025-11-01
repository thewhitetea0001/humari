import disnake
import sys, os
from disnake.ext import commands
from utilities.bot import Token

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
client.load_extension("modules.events.on_member_join")

# Cogs / slash commands
client.load_extension("modules.slash_commands.botinfo")

client.run(Token.getToken("src/config.json"))