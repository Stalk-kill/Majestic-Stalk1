import discord
from discord.ext import commands
import json
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

with open('config.json') as f:
    config = json.load(f)

@bot.event
async def on_ready():
    print("Bot ready!")
    bot.channel = bot.get_channel(int(config['audit_channel_id']))

@bot.event
async def on_member_join(member):
    e = discord.Embed(title="👤 Присоединился", color=0x00ff00)
    e.add_field(name="User", value=member.mention)
    e.add_field(name="ID", value=member.id)
    await bot.channel.send(embed=e)

@bot.event
async def on_member_remove(member):
    e = discord.Embed(title="👤 Ушёл", color=0xff0000)
    e.add_field(name="User", value=member.name)
    e.add_field(name="ID", value=member.id)
    await bot.channel.send(embed=e)

bot.run(config['token'])
