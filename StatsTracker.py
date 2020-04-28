import discord
import asyncio
from discord.ext import commands
import discord.utils
import json

ctx = commands.Bot(command_prefix='^')
amounts = {}


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @ctx.event
    async def on_ready(self):
        global amounts
        try:
            with open('amounts.json') as f:
                amounts = json.load(f)
        except FileNotFoundError:
            print("Could not load amounts.json")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == ctx.user:
            return
        # print(str(message.author) + ":")
        # print(message.content)

    @commands.command()
    async def balance(self, ctx):
        id = ctx.message.author.id
        if id in amounts:
            await ctx.send("You have {} in the bank".format(amounts[id]))
        else:
            await ctx.send("You do not have an account")

    @commands.command()
    async def register(self, ctx):
        id = ctx.message.author.id
        if id not in amounts:
            amounts[id] = 100
            await ctx.send("You are now registered")
            _save()
        else:
            await ctx.send("You already have an account")

    @commands.command()
    async def transfer(ctx, amount: int, other: discord.Member):
        primary_id = ctx.message.author.id
        other_id = other.id
        if primary_id not in amounts:
            await ctx.send("You do not have an account")
        elif other_id not in amounts:
            await ctx.send("The other party does not have an account")
        elif amounts[primary_id] < amount:
            await ctx.send("You cannot afford this transaction")
        else:
            amounts[primary_id] -= amount
            amounts[other_id] += amount
            await ctx.send("Transaction complete")
        _save()


def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)

    @commands.command()
    async def save():
        _save()


def setup(Tracker):
    Tracker.add_cog(Stats(Tracker))
