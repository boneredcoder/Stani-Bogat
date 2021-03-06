from discord.ext import commands

from bot.core.constants import Cogs
from bot.core.embeds import Top10Embed
from bot.utilities.json import return_top

class Stats:
    """ Handles these cogs - топ10, статс"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name=Cogs.Stats.top10, aliases=[Cogs.Stats.top])
    async def print_top10(self, ctx, arg): # автори or играчи
        if arg == Cogs.Stats.authors:
            authors = return_top(target='authors', how=10)
            await ctx.send(embed=Top10Embed('authors', authors))
        elif arg == Cogs.Stats.players:
            players = return_top(target='players', how=10)
            await ctx.send(embed=Top10Embed('players', players))

    # @commands.command(name='статс', aliases=['стат'])
    # async def stats(self, ctx):
    #     await ctx.send(f'<@{ctx.author.id}>, отпечатва се статистиката на юзъра.')


def setup(bot):
    bot.add_cog(Stats(bot))
