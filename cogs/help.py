import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # This replaces the default help command
    @app_commands.command(name="help", description="Open the Archive to see all available commands.")
    async def help_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="👁️ The Observer's Archive",
            description="Reading Arcus logs... Use the categories below to find information.",
            color=0x2b2d31 # Seamless Dark Mode color
        )
        
        # Using Fields to create a clean directory look
        embed.add_field(
            name="📊 Bot Information", 
            value="`/observer info` - View my technical specs and status.", 
            inline=False
        )
        embed.add_field(
            name="🏰 Server Info", 
            value="`/realm info` - Scan the current realm's data.", 
            inline=False
        )
        
        embed.set_footer(text="The Fog is ever-shifting. | Slash Commands")        
        if self.bot.user.display_avatar:
            embed.set_thumbnail(url=self.bot.user.display_avatar.url)     

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))