import disnake
import sys
from disnake.ext import commands
from utilities.log import Log

class BotInfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command()
    async def botinfo(self, inter: disnake.ApplicationCommandInteraction):
        Log.info(f"User {inter.author.name} has used the '/botinfo' command")

        embed = disnake.Embed(
            title="<:whitefrog:1428126583276961853> | Информация о боте",
            description=(
                f"<:pythonlogo:1434164317007253619> Python: `{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}`\n"
                f"<:disnakelogo:1434167456896913408> Disnake: `{disnake.__version__}`"
            ),
            color=0xcccccc
        )

        await inter.response.send_message(embed=embed)
        Log.info(f"'botinfo' embed was sended for user {inter.author.name}")
    
def setup(client):
    client.add_cog(BotInfo(client))