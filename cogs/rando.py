import discord
from discord.ext import commands
from discord import app_commands

class Rando(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rando", description="A random response from the void")
    async def rando(self, interaction: discord.Interaction):
        await interaction.response.send_message('rando?')

async def setup(bot):
    await bot.add_cog(Rando(bot))