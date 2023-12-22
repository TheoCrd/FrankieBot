from discord import Intents, Embed, Color
from discord.ext import commands
from dotenv import load_dotenv
import os
import replicate
import discord

load_dotenv()

########DISCORD INTENTS#########
intents = Intents.default()
intents.message_content = True


#######Classes Utils###############
class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(
                description=page,
                color=Color.dark_blue()
                )
            await destination.send(embed=emby)

#######COMMANDS###############
# Description
bot = commands.Bot(
    command_prefix="!",
    description="Runs a command",
    help_command=MyNewHelp(),
    intents=intents,
)


@bot.command(aliases=["sd"])
async def dream(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    msg = await ctx.send(f"“{prompt}”\n> Generating...")
    output = replicate.run(
        "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
        input={"prompt": prompt},
    )

    # Create an embed with the image
    embed = Embed(title=f"**{prompt}**", color=Color.dark_blue())
    embed.set_image(url=output[0])

    # Edit the message to include the embed
    await msg.edit(content=None, embed=embed)


bot.run(os.environ["DISCORD_TOKEN"])
