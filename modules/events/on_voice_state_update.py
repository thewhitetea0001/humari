# thanks: stackoverflow.com/questions/76784675/disnake-py-private-voice-channel-continuation-of-work
# :3

import disnake
import asyncio
from disnake.ext import commands, tasks
from asyncio import sleep
from utilities.log import Log

class OnStateVoiceUpdate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = after.channel or before.channel
        if channel.id != 1435241015693807626:
            return
        
        Log.info("event", "on_voice_state_update", f"({member.name}) User joined the '{channel.id}' channel")
        
        category = after.channel.category if after.channel else before.channel.category
            
        channel = await member.guild.create_voice_channel(
            name=f"{member.display_name}",
            category=category
        )
        Log.info("event", "on_voice_state_update", f"({member.name}) Successfully created new voice channel with '{channel.name}' name")

        await channel.set_permissions(
            member,
            connect=True,
            mute_members=True,
            move_members=True,
            manage_channels=True
        )
        Log.info("event", "on_voice_state_update", f"({member.name}) Successfully modified '{channel.id}' ({channel.name}) channel permissions")

        await member.move_to(channel)
        Log.info("event", "on_voice_state_update", f"Successfully moved user '{member.name}' to '{channel.id}' ({channel.name}) channel")

        def check_leave(m, b, a):
            return m == member and b.channel == channel and a.channel is None and len(b.channel.members) == 0
        
        def check_join(m, b, a):
            return m == member and b.channel is None and a.channel == channel and len(a.channel.members) == 0
        
        while True:
            await self.client.wait_for('voice_state_update', check=check_leave)

            try:
                await self.client.wait_for('voice_state_update', check=check_join, timeout=1.0)
            except asyncio.TimeoutError:
                Log.warn("event", "on_voice_state_update", f"Timeout error from '{channel.id}' ({channel.name}) channel")
                await channel.delete()
                Log.info("event", "on_voice_state_update", f"Successfully deleted '{channel.id}' ({channel.name}) channel")
                break

def setup(client):
	client.add_cog(OnStateVoiceUpdate(client))