import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 1. Custom Bot Class
class TheObserver(commands.Bot):
    def __init__(self):
        # Setup Intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        super().__init__(
            command_prefix="!", 
            intents=intents, 
            help_command=None
        )

    # 2. Setup Hook (Runs before the bot connects)
    async def setup_hook(self):
        # Load Cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f'📦 Loaded Cog: {filename}')

        # 3. Sync Slash Commands
        # This makes the / commands show up in Discord
        await self.tree.sync()
        print('📡 Slash commands synced globally')

    async def on_ready(self):
        print(f'✅ Logged in as {self.user}')
        print('--------------------------')

# 4. Initialize and Run
bot = TheObserver()

async def main():
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Handles Ctrl+C gracefully
        pass