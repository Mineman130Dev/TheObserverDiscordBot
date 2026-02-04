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

    async def setup_hook(self):
        # 1. Load Cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f'📦 Loaded Cog: {filename}')

        # 2. THE CLEANER: Run this to wipe the double commands from your test server
        GUILD_ID = 1467059579795017874 
        guild = discord.Object(id=GUILD_ID)
        
        # This clears the "Guild Bucket" to stop the double commands
        self.tree.clear_commands(guild=guild)
        await self.tree.sync(guild=guild)
        
        # This syncs the "Global Bucket" (the one you want to keep)
        await self.tree.sync()
        
        print(f"🧹 Commands cleared for guild {GUILD_ID} and synced globally!")

    async def on_ready(self):
        # Alternatives: discord.Game(name="...")
        activity = discord.Activity(type=discord.ActivityType.watching, name="Arcus logs | /help")
        
        await self.change_presence(status=discord.Status.online, activity=activity)
        
        print(f'✅ Logged in as {self.user}')
        print('---------------------------')

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