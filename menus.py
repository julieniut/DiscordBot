import os
from dotenv import load_dotenv
import discord
from discord.ui import Select, View
from discord.ext import commands

load_dotenv() # Load the .env file

TOKEN = os.getenv("DISCORD_TOKEN") # Get the token from the .env file

bot = commands.Bot(command_prefix='{', intents=discord.Intents.all()) 

@bot.event 
async def on_ready(): 
    print(f"{bot.user.name} has connected to Discord!") # Prints "Bot has connected to Discord!"
    await bot.change_presence(activity=discord.Game(name="Je suis un sale connard qui marche pas")) # Change the bot's activity

@bot.command()
async def menus(ctx): 
    budget = Select( 
        placeholder="Selectionnez votre budget",
        options=[
            discord.SelectOption(
                label="Petite faim",
                emoji="🍟", 
                description="De 800 à 1000€"),
            discord.SelectOption(
                label="Grosse faim", 
                emoji="🍔", 
                description="De 1000 à 1500€"),
            discord.SelectOption(
                label="Petage de bide", 
                emoji="🍗", 
                description="De 1500 à 2000€")
        ]
    )

    async def budget_callback(interaction):
        if interaction.data["values"][0] == 'Petite faim':
            await interaction.response.send_message(f"Alors comme ça on a une petite faim")
        return interaction.data["values"][0]
    
    usage = Select(
        placeholder="Selectionnez votre utilisation",
        options=[
            discord.SelectOption(
                label="Secretaire",
                emoji="📝",
                description="Bureautique simple"),
            discord.SelectOption(
                label="Gamer",
                emoji="🎮",
                description="Tout sauf fotrnite"),
            discord.SelectOption(
                label="Machine de travail",
                emoji="🔧",
                description="Besoin de fiabilitée")
            ]
        )

    async def usage_callback(interaction):
        if interaction.data["values"][0] == 'Secretaire':
            await interaction.response.send_message(f"Alors comme ça on écrit pas vite")

    usage.callback = usage_callback
    budget.callback = budget_callback
    print(budget.callback)
    view = View()
    view.add_item(budget)
    view.add_item(usage)
    await ctx.send("Des configurations de pc mise à jour régulièrement pour vous !", view=view)

bot.run(TOKEN)
