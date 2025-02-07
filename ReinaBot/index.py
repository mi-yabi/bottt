import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Set bot activity
    activity = discord.Game("Playing a game")  # Change "Playing a game" to your custom status
    await bot.change_presence(status=discord.Status.online, activity=activity)

bot.run('TOKEN')
