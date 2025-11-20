import disnake
import psutil, os
import sys
from disnake.ext import commands
from utilities.log import Log
from utilities.bot import Icons, UpTime

class BotInfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command()
    async def botinfo(
        self, 
        inter: disnake.ApplicationCommandInteraction
    ):
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

        process = psutil.Process(os.getpid())
        ram_used = f"{process.memory_info().rss / 1024 ** 2:.2f}"

        Log.info("scmd", "botinfo", f"({inter.author.name}) User used the command")

        embed = disnake.Embed(
            title=f"{Icons.Server.white_frog} | Информация о боте",
            description=(
                f"{Icons.Dev.python_logo} Python: `{python_version}`\n"
                f"{Icons.Dev.disnake_logo} Disnake: `{disnake.__version__}`\n\n"
                f"{Icons.Dev.boat_green} Аптайм: {UpTime.getUpTime()}\n"
                f"{Icons.Dev.boat_green} RAM использовано: `{ram_used}` MB"
            ),
            color=0x91918f
        )

        embed.set_footer(
            text=f"Запросил {inter.author.name}",
            icon_url=f"{inter.author.display_avatar.url}",
        )

        await inter.response.send_message(embed=embed)
        Log.info("scmd", "botinfo", f"Embed was sended for user {inter.author.name}")
    
def setup(client):
    client.add_cog(BotInfo(client))