import discord
from discord.ext import commands
from discord import app_commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Bot info group
    observer_group = app_commands.Group(name="observer", description="Commands related to The Observer bot")

    @observer_group.command(name="info", description="View technical specs and status of The Observer")
    async def about_bot_info(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📊 Statistics for The Observer",
            description="Here is my up to date info!",
            color=0x3498db
        )
        embed.add_field(name="Author", value="Mineman130", inline=True)
        embed.add_field(name="Version", value="1.1.0", inline=True)
        embed.add_field(name="Language", value="Python 3.14\n(discord.py)", inline=True)
        embed.add_field(
            name="What do I do?", 
            value="I help manage the server and provide\nuseful info to members! Type `!help` to see more.", 
            inline=False
        )
        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)

    # Server info group
    realm_group = app_commands.Group(name="realm", description="Commands related to this server")

    @realm_group.command(name="info", description="Scan the current realm's data and statistics")
    async def realm_info(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(
            title=f"📊 Statistics for {guild.name}",
            description="Here is the current breakdown of our server.\n\n**[Join our Server!](https://discord.gg/WZnrwJr3Hh)**",
            color=discord.Color.green()
        )

        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        owner_mention = guild.owner.mention if guild.owner else "Unknown"
        embed.add_field(name="Owner", value=owner_mention, inline=True)
        embed.add_field(name="Members", value=f"{guild.member_count} users", inline=True)
        embed.add_field(name="Boosts", value=f"Level {guild.premium_tier}", inline=True)
        embed.add_field(name="Permanent Invite", value="https://discord.gg/WZnrwJr3Hh", inline=False)

        created_at = guild.created_at.strftime("%b %d, %Y")
        embed.add_field(name="Created On", value=created_at, inline=False)
        embed.set_footer(text=f"Server ID: {guild.id}")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))