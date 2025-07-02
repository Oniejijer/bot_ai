import discord
from discord.ext import commands
from discord import app_commands
from model import get_class


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


GUILD_ID  = discord.Object(id=1331418136087494657)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(file_name)
            await ctx.send("Archivo guardado")
            class_name = get_class("keras_model.h5", "labels.txt", file_name)
            await ctx.send()

            try:
                class_name = get_class("keras_model.h5", "labels.txt", file_name)
                if class_name[0] == "Lapiz/Crayon":
                    await ctx.send("Esto es un lapiz/crayon, comnunmente usado para colorear o escribir. La marca mas vendida de ellas es Crayola.")

                elif class_name[0] == "Audifonos":
                    await ctx.send("Estos son audifonos, tienen distintas funciones. Las marcas vendidas en el mundo son Apple, Samsung, Y JBL. ")
                
                elif class_name[0] == "Libros":
                    await ctx.send("Este es un libro, u libreta. El libro mas vendido del mundo es la Biblia.")

            except:
                await ctx.send("La clasificacion ha fallado")       
    else: 
        await ctx.send("No hay archivos adjuntos")

bot.run("MTM4NzIyNzY1MDQ0NzExNDQxMw.G-qV66.cHJlZcsPUvn-affX3vlZmt3_b-nUyRGN1NNt7E")