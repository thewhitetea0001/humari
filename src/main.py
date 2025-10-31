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

# Cogs
client.load_extension("modules.events.on_ready")
client.load_extension("modules.events.on_member_join")

client.run(Token.getToken("src/config.json"))