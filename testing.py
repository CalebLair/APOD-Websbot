from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.command(name="idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")


with open("Hidden.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Bot Online!")
    bot.run(TOKEN)
