import discord
from discord import Intents
from discord.ext import commands, tasks
from itertools import cycle
import wolframalpha

intents = Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)
status = cycle(['!solve'])

@bot.event
async def on_ready(): change_status.start() 
print("[+] Ready")

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
# Initialize the Wolfram Alpha client
client = wolframalpha.Client('id')

@bot.command()
async def solve(ctx, *, problem):
    try:
        # Use the Wolfram Alpha API to solve the problem
        res = client.query(problem)

        # The Wolfram Alpha API returns multiple possible solutions,
        # so we'll just take the first one
        solution = next(res.results).text

        # Send the solution to the user
        await ctx.send(solution)
    except Exception as e:
        # If an error occurs, send a message to the user
        await ctx.send(f"An error occurred. I guess you aren't worthy. Unless you're IntrepidBird. Then I apologize sincerely. Try again.")

bot.run('token')

