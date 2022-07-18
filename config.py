import interactions
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio
import datetime 
from datetime import datetime

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

bot = interactions.Client(token=TOKEN)

@bot.command(
    name="config",
    description="Pour demander une configuration",
    scope=996907904324091944,
    options=[
        interactions.Option(
            name="1500",
            description="description_1",
            type=interactions.OptionType.SUB_COMMAND,
            # options=[
            #     interactions.Option(
            #         name="option",
            #         description="A descriptive description",
            #         type=interactions.OptionType.INTEGER,
            #         required=False,
            #     ),
            # ],
        ),
    ],
)
async def cmd(ctx: interactions.CommandContext, sub_command: str, second_option: str = "", option: int = None):
    if sub_command == "1500":
      await ctx.send(f"Link of the first config")
    elif sub_command == "2000":
      await ctx.send(f"Link of the second")


@bot.command()
async def c(ctx):
    messages = await ctx.channel.history(limit=1).flatten()
    for each_message in messages:
        await each_message.delete()
    embed = discord.Embed(
    title="Commandes",
    description= "\n{menus (Affiche menu des configs)"
    "\n!del 'n' supprimer 'n' message "
    "\n!cmos (Montre comment faire un CMOS)"
    "\n!temp (Un tuto pour check les température)"
    "\n!xmp  (Activer l'xmp dans son bios)"
    "\n!key (Lien d'achat clé W10 Pro)",
        url="https://github.com/MerlinConnected/DiscordBot",
        timestamp=datetime.now(), 
        color=0x1abc9c
    )
    msg = await ctx.send(embed=embed)

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()

    for each_message in messages:
        await each_message.delete()

@bot.command()
async def cmos(ctx):
    messages = await ctx.channel.history(limit=1).flatten()
    for each_message in messages:
        await each_message.delete()
    await ctx.send("Par ici le clear CMOS --> https://www.youtube.com/watch?v=Fc0HIDKC1U0")    

@bot.command()
async def temp(ctx):
    messages = await ctx.channel.history(limit=1).flatten()
    for each_message in messages:
        await each_message.delete()
    await ctx.send("Pour vérifier les températures de votre processeur :"
"\n- Télécharger OCCT : https://www.ocbase.com/download"
"\n- Fermer tous les programmes (Discord, Steam...)"
"\n- Lancer OCCT "
"\n- Aller dans l'onglet : 'Test' (colonne de gauche)"
"\n- Sélectionner dans la partie planning des tests : 'CPU' "
"\n- Définir la durée du test --> 15 minutes minimum (en cliquant sur le logo infini au dessus)"
"\n- Tout laisser en auto et appuyer sur play "
"\n- Une fois le test terminé, envoyez dans le salon discord un screen des températures de votre processeur qui se trouvent dans la partie 'Monitoring' (à droite)."
"\nExemple ici: https://imgur.com/a/5oWKVfp")

@bot.command()
async def xmp(ctx):
    messages = await ctx.channel.history(limit=1).flatten()
    for each_message in messages:
        await each_message.delete()
    await ctx.send("Pour activer l'XMP --> https://www.youtube.com/watch?v=3t6J1EiHb_w")

@bot.command()
async def key(ctx):
    messages = await ctx.channel.history(limit=1).flatten()
    for each_message in messages:
        await each_message.delete()
    await ctx.send("Une clé d'activation Windows 10 Pro pas cher ? \nC'est par ici ! -->  https://bit.ly/3jUPNTP \nIl ne s'agit pas d'une livraison instantanée donc patiente le temps que le site t'envoie la clé par mail :slight_smile:")

bot.start()
