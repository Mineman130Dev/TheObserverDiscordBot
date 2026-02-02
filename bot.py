import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# 1. Setup Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# 2. Define the Bot
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# 3. Cog Loader
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')
    print('--- Cogs Loaded ---')

# 4. Main Entry Point
async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

# Start the bot
if __name__ == "__main__":
    asyncio.run(main())