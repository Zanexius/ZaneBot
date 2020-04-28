import discord
import asyncio
from discord.ext import commands
import discord.utils
from random import randint

bot = commands.Bot(command_prefix='^')


class Emotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == bot.user:
            return
        # print(str(message.author) + ":")
        # print(message.content)

    @commands.command()
    async def vibecheck(self, ctx):
        number = randint(1,5)
        if number == 1:
            await ctx.send('Uncultured chach')
        elif number == 2:
            await ctx.send('You dry chunk of tofu how dare you')
        elif number == 3:
            await ctx.send('omg stop pinning things')
        elif number == 4:
            await ctx.send('Zane we need a vibe check feature on the bot https://cdn.discordapp.com/emojis/670004631996334093.gif?v=1')
        elif number == 5:
            await ctx.send('produce me your flat ass')


#https://cdn.discordapp.com/attachments/543637392158883870/704360845014073414/Rex.jpg
    @commands.command()
    async def Rex(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/543637392158883870/704360845014073414/Rex.jpg')

    @commands.command()
    async def yay(self, ctx):
        await ctx.send('<:PandaDuck:478315152362700808>')

    @commands.command()
    async def comfy(self, ctx):
        await ctx.send('<:GoodMorning:636731906737569813>')

    @commands.command()
    async def aww(self, ctx):
        await ctx.send('<:GengarAww:636731906721054730>')

    @commands.command()
    async def pokeup(self, ctx):
        await ctx.send('<:KyuHide:636731910055395329>')

    @commands.command()
    async def smirk(self, ctx):
        await ctx.send('<:pikachu_smirk_right:636731912009941051>')

    @commands.command()
    async def megusmirk(self, ctx):
        await ctx.send('<:megusmirk:636731911028342794>')

    @commands.command()
    async def owowhatsthis(self, ctx):
        await ctx.send('<a:owowhatsthis:636734108839575554>')

    @commands.command()
    async def hype(self, ctx):
        await ctx.send('<a:pandaHYPE:636734109430972448>')

    @commands.command()
    async def trash(self, ctx):
        await ctx.send('<a:Rainbow_Blob_Trash:636734109200154654>')

    @commands.command()
    async def REE(self, ctx):
        await ctx.send('<a:ReeGun:636734109271719937>')

    @commands.command()
    async def welcome(self, ctx):
        await ctx.send('<a:We:636741200082108436>' + '<a:lcome:636741199662678047>')

    @commands.command()
    async def bongocat(self, ctx):
        await ctx.send('<a:bongocat:637401077666414638>')

    @commands.command()
    async def pingREE(self, ctx):
        await ctx.send('<a:PandaPingRee:637401077368619060>')


def setup(botEmotes):
    botEmotes.add_cog(Emotes(botEmotes))
