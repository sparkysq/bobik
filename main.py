import config
import discord
from youtube_dl import YoutubeDL
from discord.ext import commands


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#Опции 
YDL_OPTIONS = {'format' : 'worsaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'key': 'FFmpegExtractAudio' }
FFMPEG_OPTIONS = {'before_options': "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", 'options': '-vn'}



@bot.command()
async def play(ctx, url):
    vc = await ctx.mesage.author.voice.channel.connect()
    
    with YoutubeDL(YDL_OPTIONS) as ydl:
        if 'https://' in url:
            info = ydl.extract_info(url, download=False)
        else:
            info = ydl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]

    link = info['formats'][0]['url']

    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=link, **FFMPEG_OPTIONS))

#client.run(config.token)
bot.run(config.token)