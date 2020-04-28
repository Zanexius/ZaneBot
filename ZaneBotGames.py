import discord
import asyncio
from discord.ext import commands
import discord.utils
from random import randint

bot = commands.Bot(command_prefix='^')


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == bot.user:
            return
        # print(str(message.author) + ":")
        # print(message.content)

    @commands.command()
    async def GuessGame(self, ctx):
        await ctx.send('Starting Guessing Game...')
        await ctx.send('Guess a number from 1-6!')

        def answer():
            diceanswer = randint(1, 6)
            return diceanswer

        correct = str(answer())
        endgame = False
        print(correct)
        while not endgame:
            # PROBLEM IS THIS WAIT_FOR. Its not getting past the await. I think its not picking up my messages
            # could try just a sleep for 10 secs or somethin, look up async sleeps
            # self.useranswer = await bot.wait_for('message', timeout=10)
            useranswer = await self.bot.wait_for('message', timeout=10)
            if useranswer.content == correct:
                await ctx.send('Correct!')
                endgame = True
            else:
                await ctx.send('Try Again(1-6)!')

    @commands.command()
    async def Random(self, ctx):
        await ctx.send('Enter your range (Separate lines):')
        input1 = await self.bot.wait_for('message', timeout=10)
        input2 = await self.bot.wait_for('message', timeout=10)
        await ctx.send('Random number (' + input1.content + '-' + input2.content + '): ' + str(randint(int(input1.content), int(input2.content))))


def setup(botGames):
    botGames.add_cog(Games(botGames))
