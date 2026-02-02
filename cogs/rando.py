import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

class Rando(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def rando(self, ctx):
        await ctx.send('rando?')

async def setup(bot):
    await bot.add_cog(Rando(bot))