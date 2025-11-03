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
        user: disnake.User = None,
    ):
        try:
            if user is None or user is inter.author:
                user = inter.author
                text = "Вы погладили себя!"
            elif user.id == 1429583271473184878:
                text = "Вы погладили меня! Спасибо <3"
            else:
                text = f"Вы погладили <@{user.id}>!"

            Log.info("scmd", "patpat", f"User {inter.author.name} -> {user}")

            response = requests.get(user.display_avatar.url)
            avatar = BytesIO(response.content)

            petpet.make(avatar, "assets/petpet_avatar.gif")

            await inter.response.send_message(
                text,
                file=disnake.File("assets/petpet_avatar.gif"
            ))
            
            Log.info("scmd", "patpat", f"Message was successfully sent")
        except Exception as e:
            await inter.response.send_message(f"Ошибка при выполнении команды:\n```sh\n{e}\n```", ephemeral=True)
            Log.error("scmd", "patpat", f"({inter.author.name}) {e}")

def setup(client):
    client.add_cog(PatPat(client))