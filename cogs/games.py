from discord.ext import commands
from discord.utils import get

from models import GameManager


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.manager = GameManager()

    @commands.command(name='tic-tac-toe', aliases=['ttt'])
    async def tic_tac_toe(self, ctx, option, *args):
        if option == 'invite':
            if len(args) == 1:
                invite_nick_name = args[0]
                target_user = get(ctx.guild.members, name=invite_nick_name)

                if ctx.message.author.id == target_user.id:
                    await ctx.send('You cant play by yourself :c')
                    return

                if target_user is None:
                    await ctx.send('Cant find member with this nickname :c')
                    return

                lobby = self.manager.invite(ctx.message.author, target_user, 'TicTacToe')
                await ctx.send(f'{target_user.mention},\n'
                               f'User {ctx.message.author} sent you an invite to play Tic-tac-toe\n'
                               f'To accept the invite use /ttt respond [id]({lobby.id}) [answer](+/- or y/n)')


def setup(bot):
    bot.add_cog(Games(bot))
