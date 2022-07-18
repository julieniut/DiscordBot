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
    embed = discord.Embed(
    title="Commandes",
    description= "\n{menus Affiche les configs"
    "\n!del 'n' supprimer 'n' message "
    "\n!cmos ",
        url="https://github.com/MerlinConnected/DiscordBot",
        timestamp=datetime.now(), 
        color=0x1abc9c
    )
    msg = await ctx.send(embed=embed)

@bot.command(name="del")
async def delete(ctx, amount = 2):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def cmos(ctx):
	await ctx.send("Par ici le clear CMOS --> https://www.youtube.com/watch?v=Fc0HIDKC1U0")


bot.start()
