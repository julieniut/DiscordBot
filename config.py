import interactions
import os
from dotenv import load_dotenv

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



bot.start()
