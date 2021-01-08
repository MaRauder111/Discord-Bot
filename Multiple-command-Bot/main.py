import discord
import os
import requests
from discord.ext import commands
from alive import keep_alive

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
  print(f'{bot.user.name} has connected to Discord!')

#check ping
@bot.command()
async def ping(ctx):
  await ctx.send(f'My ping is {bot.latency}!')

#say hello
@bot.command()
async def hello(ctx):
  await ctx.send('Hello I am multiple command bot')

#clear chat
@bot.command()
async def clear(ctx, amount = 10):
  await ctx.channel.purge(limit=amount)

#slap anyone
@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

#weather
@bot.command()
async def weather(ctx):
  res = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Imphal&appid=Use_your_own_weather_api&units=metric")
  data = res.json()
  temp = data['main']['temp']
  await ctx.channel.send(temp)

#check server owner
@bot.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


keep_alive()
bot.run(os.getenv('TOKEN'))
