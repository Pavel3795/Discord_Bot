import os
import discord
from discord.ext import commands
from random import choice
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Всегда следи за природой, не загрязняй её и не позволяй это делать кому то))). 😉')

@bot.command()
async def garbage(ctx):
    await ctx.send(f' Ты нашёл мусор, теперь попытайся найти завод по переработке мусора и здай его. Всегда делай мир чище.:thumbsup:')

@bot.command()
async def mem(ctx):
    image_name = choice(os.listdir('images'))
    with open(f'images/{image_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def functions(ctx):
    await ctx.send(f'Вот все мои функции. $hello; $garbage; $mem; $functions. Приятного использования:upside_down: ')


bot.run("MTEwOTg0NjkzMDY1NTI4OTM0NA.GUYUQE.LChGXStB-0sZt1iL5goT4NH_itbpt-LjnrNfUE")





#@bot.command()
#async def heh(ctx, count_heh = 5):
#    await ctx.send("he" * count_heh)