import disnake
from disnake.ext import commands
import json
import sys, os

# Go to parrent dir
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def get_token():
    with open("src/config.json", "r") as f:
        data = json.load(f)

    token = data["client"]["token"]
    return token;

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

client.run(get_token())
