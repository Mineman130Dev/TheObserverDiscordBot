import discord
from discord.ext import commands
from discord import app_commands

class Summon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="summon", description="Summon The Observer to the chat")
    async def rando(self, interaction: discord.Interaction):
        await interaction.response.send_message('Hmm?')

async def setup(bot):
    await bot.add_cog(Summon(bot))