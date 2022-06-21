import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='.')
@bot.command()
async def elker(ctx):
    await ctx.send('https://stackoverflow.com/questions/63348991/how-do-i-mention-user-through-discord-bots-python')

@bot.command()
async def m(ctx, self):
    await ctx.send(self)

@bot.command()
async def  s (ctx, message):
    await ctx.send(message)

#eventoss
@bot.event
async def on_ready():
     print('We have logged in as {0.user}'.format(bot))

async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))




bot.run('NzAxMTc1NzUyMzQyNzY1NTc5.Xptq7A.JiBvxooU2N7P4So0hMMwvp6qBfA')
