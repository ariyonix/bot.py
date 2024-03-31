import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def katıldı(ctx, member: discord.Member):
    await ctx.send(f'{member.name} katıldı {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def emoji1(ctx):
    await ctx.send("\U0001f600")

@bot.command()
async def emoji2(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def emoji3(ctx):
    await ctx.send("\U0001F606")

@bot.command()
async def emoji4(ctx):
    await ctx.send("\U0001F923") 

@bot.command()
async def emoji5(ctx):
    await ctx.send("\U0001F945")

@bot.command()
async def emoji6(ctx):
    await ctx.send("\U0001f756")

@bot.command()
async def emoji7(ctx):
    await ctx.send("\U0001f875")

@bot.command()
async def emoji8(ctx):
    await ctx.send("\U0001f985")

@bot.command()
async def emoji9(ctx):
    await ctx.send("\U0001f578")

@bot.command()
async def emoji10(ctx):
    await ctx.send("\U0001f786")    

@bot.command()
async def emoji11(ctx):
    await ctx.send("\U0001f362")

@bot.command()
async def emoji12(ctx):
    await ctx.send("\U0001f999")

@bot.command()
async def emoji13(ctx):
    await ctx.send("\U0001f687")

@bot.command()
async def emoji14(ctx):
    await ctx.send("\U0001F463")

@bot.command()
async def emoji15(ctx):
    await ctx.send("\U0001F364")

@bot.command()
async def python(ctx):
    await ctx.send("Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir. Girintilere dayalı basit söz dizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır.")

@bot.command()
async def Java(ctx):
    await ctx.send("Java, Sun Microsystems tarafından üretilen ve yazılım uygulamaları geliştirmeye yardımcı yazılımlar bütünüdür. Java'nın kullanım alanı gömülü aygıtlardan cep telefonlarına, kurumsal sunuculardan süper bilgisayarlara uzanmaktadır.")

@bot.command()
async def C(ctx):
    await ctx.send("C programlama dili, UNIX işletim sistemini geliştirmek için B dili kullanılarak üretilen bir programlama dilidir.")

@bot.command()
async def iletişim(ctx):
    await ctx.send("iletişim için kilicahmetkayra1@gmail.com'a mail gönderebilirsiniz.")

@bot.command()
async def komutlar(ctx):
  await ctx.send("Şuanda 24 komut bulunmaktadır.")

bot.run("token")
