import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group(name="observer", invoke_without_command=True, case_insensitive=True)
    async def observer_info_group(self, ctx):
        await ctx.send("Try typing `!bot info`!")

    @observer_info_group.command(name="info")
    async def about_bot_info(self, ctx):
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
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    # Server info group
    @commands.group(name="realm", invoke_without_command=True, case_insensitive=True)
    async def realm(self, ctx):
        await ctx.send("Try typing `!server info` to see details about this place!")

    @realm.command(name="info")
    async def realm_info(self, ctx):
        guild = ctx.guild
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

        await ctx.send(embed=embed)

# This part is crucial for loading the cog
async def setup(bot):
    await bot.add_cog(Info(bot))