import disnake
from utilities.log import Log
from disnake.ext import commands

class OnMemberJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        Log.info(f"User '{member.name}' ({member.id}) has joined the server")

        channel = self.client.get_channel(1428122936144953344)
        embed_thumbnail_url = "https://media.discordapp.net/attachments/1428121559872176320/1433870443777097889/green_grog22.png?ex=69064369&is=6904f1e9&hm=bc2993f50d9ba5e7496b669d872889b52a0987b518badc37480b26e3254eb777&=&format=webp&quality=lossless&width=137&height=122"

        embed = disnake.Embed(
            title=f"Добро пожаловать, {member.name}!",
            description=f"Привет, <@{member.id}>! Мы очень рады, что ты решил зайти на наш сервер. Ознакомься с правилами в канате <#1428120984011149424>, и можешь начинать начинай общение. Удачи!",
            color=0x3aa33a
        )
        
        embed.set_thumbnail(url=embed_thumbnail_url)

        await channel.send(embed=embed)
        Log.info("The greating embed for membed '{member.name}' was sended to the channel 'channel.id'")

def setup(client):
	client.add_cog(OnMemberJoin(client))
