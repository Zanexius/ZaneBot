import discord
from discord.ext import commands


class Tests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def AmI(self, ctx):
        """Says if a user is cool.
        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

    # the main command that sub commands reference to need a @commands.group
    # sub-commands go by the @maincommand.command()
    # In discord, command would be ^cool _bot ZaneBot
    @AmI.command()
    async def cool(self, ctx):
        """Is the bot cool?"""
        await ctx.send('Yes, {} is cool.'.format(ctx.message.content.replace('^AmI cool ', '')))

    @AmI.command()
    async def awesome(self, ctx):
        await ctx.send('Hell no, u ugly bruh')


def setup(bot):
    bot.add_cog(Tests(bot))
