import discord
import random
import os
import json
from discord.ext import commands
from discord import app_commands

class Slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emojis = ["🍎", "🍑", "🍋", "🍐", "💎", "7️⃣"]
        self.data_file = "bank.json"

    # --- Data Helpers ---
    def load_bank(self):
        # Create the file if it doesn't exist so it doesn't crash
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as f:
                json.dump({}, f)
        
        with open(self.data_file, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def save_bank(self, data):
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def get_user_bank(self, user_id):
        bank = self.load_bank()
        uid = str(user_id)
        if uid not in bank:
            bank[uid] = 100 #Starting money if new player
            self.save_bank(bank)
        return bank, uid

    # --- Commands ---

    @app_commands.command(name="balance", description="Check your current point balance.")
    async def balance(self, interaction: discord.Interaction):
        bank, uid = self.get_user_bank(interaction.user.id)
        amt = bank[uid]
        await interaction.response.send_message(f"💰 You currently have **{amt}** points.")

    @app_commands.command(name="guess", description="Guess a number 1-10 to win 5 points!")
    async def guess(self, interaction: discord.Interaction, number: int):
        if number < 1 or number > 10:
            await interaction.response.send_message("Please guess between 1 and 10!", ephemeral=True)
            return

        bank, uid = self.get_user_bank(interaction.user.id)
        winning_number = random.randint(1, 10)
        
        if number == winning_number:
            bank[uid] += 5
            self.save_bank(bank)
            color = 0x00FF00
            msg = f"🎯 **Direct Hit!** The number was {winning_number}. You won **5 points**!"
        else:
            color = 0xFF0000
            msg = f"❌ **Missed!** The number was {winning_number}. Your guess: {number}."

        embed = discord.Embed(title="🎯 Number Guess", description=msg, color=color)
        embed.set_footer(text=f"New Balance: {bank[uid]}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="slots", description="Bet points on the slots!")
    async def slots(self, interaction: discord.Interaction, bet: int):
        bank, uid = self.get_user_bank(interaction.user.id)
        balance = bank[uid]

        if bet <= 0:
            await interaction.response.send_message("You have to bet at least 1 point!", ephemeral=True)
            return
        
        if bet > balance:
            await interaction.response.send_message(f"You're too broke! Your balance is only **{balance}**.", ephemeral=True)
            return

        # Roll symbols
        s1, s2, s3 = [random.choice(self.emojis) for _ in range(3)]
        machine = f"**[ {s1} | {s2} | {s3} ]**"

        if s1 == s2 == s3:
            winnings = bet * 10
            bank[uid] += winnings
            result = f"{machine}\n**JACKPOT!** You won {winnings} points!"
            color = 0x00FF00
        elif s1 == s2 or s2 == s3 or s1 == s3:
            winnings = bet * 2
            bank[uid] += winnings
            result = f"{machine}\n**Small Win!** You won {winnings} points."
            color = 0xFFFF00
        else:
            bank[uid] -= bet
            result = f"{machine}\n**Loss.** You lost {bet} points."
            color = 0xFF0000

        self.save_bank(bank)
        
        embed = discord.Embed(title="🎰 Slots Result", description=result, color=color)
        embed.set_footer(text=f"New Balance: {bank[uid]}")
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Slots(bot))