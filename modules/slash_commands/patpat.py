import requests
import disnake
from disnake.ext import commands
from utilities.log import Log
from io import BytesIO
from petpetgif import petpet

class PatPat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    async def patpat(
        self,
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.Member = None,
    ):
        text = f"Вы погладили <@{user.id}>!"

        if user == None:
            user = inter.author
            text = "Вы погладили себя!"
        
        if user.id == 1429583271473184878:
            text = "Вы погладили меня! Спасибо <3"

        Log.info(f"User {inter.author.name} has used the '/patpat {user}' command")

        response = requests.get(user.display_avatar.url)
        avatar = BytesIO(response.content)

        petpet.make(avatar, "assets/petpet_avatar.gif")

        await inter.response.send_message(
            text,
            file=disnake.File("assets/petpet_avatar.gif"
        ))
        
        Log.info(f"User {inter.author} petted {user}")

def setup(client):
    client.add_cog(PatPat(client))