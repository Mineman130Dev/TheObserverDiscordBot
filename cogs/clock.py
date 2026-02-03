import discord
from discord.ext import commands
from discord import app_commands

class Clock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clock", description="Have the Observer clock that tea 🤏")
    async def clock(self, interaction: discord.Interaction):
        await interaction.response.send_message('🤏🤏🤏')

async def setup(bot):
    await bot.add_cog(Clock(bot))