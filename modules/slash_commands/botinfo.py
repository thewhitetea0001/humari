import disnake
import sys
from disnake.ext import commands
from utilities.log import Log
from utilities.bot import Icons

class BotInfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command()
    async def botinfo(
        self, 
        inter: disnake.ApplicationCommandInteraction
    ):
        Log.info(f"User {inter.author.name} has used the '/botinfo' command")

        embed = disnake.Embed(
            title=f"{Icons.Server.white_frog} | Информация о боте",
            description=(
                f"{Icons.Dev.python_logo} Python: `{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}`\n"
                f"{Icons.Dev.python_logo} Disnake: `{disnake.__version__}`"
            ),
            color=0xcccccc
        )

        embed.set_footer(
            text=f"Запросил {inter.author.name}",
            icon_url=f"{inter.author.display_avatar.url}",
        )

        await inter.response.send_message(embed=embed)
        Log.info(f"'botinfo' embed was sended for user {inter.author.name}")
    
def setup(client):
    client.add_cog(BotInfo(client))