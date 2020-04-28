import discord
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix='^')


class Games(commands.Cog):

    @bot.command()
    async def joined(self, ctx, *, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


def setup(bot):
    bot.add_cog(Games(bot))
