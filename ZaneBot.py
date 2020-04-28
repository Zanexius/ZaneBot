import discord
import discord.utils
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='^')

startup_extensions = ["tests", "TestBot", "ZaneBotGames", "simple", "Emotes"]

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


@bot.command()
async def load(ctx, extension_name: str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))


# @bot.command()
# async def GuessGame(ctx):
#     await ctx.send('Starting Guessing Game...')
#     await ctx.send('Guess a number from 1-6!')
#
#     def answer():
#         diceanswer = randint(1, 6)
#         return diceanswer
#
#     correct = str(answer())
#     endgame = False
#     print(correct)
#     while not endgame:
#         # PROBLEM IS THIS WAIT_FOR. Its not getting past the await. I think its not picking up my messages
#         # could try just a sleep for 10 secs or somethin, look up async sleeps
#         # self.useranswer = await bot.wait_for('message', timeout=10)
#         useranswer = await bot.wait_for('message', timeout=10)
#         print("got input")
#         await ctx.send(correct + ', ' + useranswer.content)
#         if useranswer.content == correct:
#             await ctx.send('Correct!')
#             endgame = True
#         else:
#             await ctx.send('Try Again(1-6)!')

@bot.command()
async def unload(ctx, extension_name: str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name))


@bot.command()
async def info(ctx):
    """Gives info about bot"""
    embed = discord.Embed(title="Zane Bot", description="All hail the hypnotoad!", color=0x0091C5)

    # give info about you here
    embed.add_field(name="Author", value="Zanexius")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)


# ctx.send('String')
# ctx.author references to the user that activated the command
# ctx.command references the name of the command called
# ctx.prefix references the prefix used to call the command
# adding a description in @bot.command() will add a description after you ^help commandname
# briefs go after you call ^help to give you a brief description of the commands
# can't really do name='' in @bot.command() because if u use multi word names, sub commands wont work

@bot.command()
async def check(ctx):
    await ctx.send(str(ctx.message.author))


############################

@bot.event
async def on_member_join(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, ctx.message.author)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@bot.event
async def update_data(users, user):
    print(user.id)
    print(bot.get_user(user.id))

    if f'{user.id}' not in users and f'{user}' != 'ZaneBot#7121':
        print('*New User Added')
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(round((20 * experience) ** (1 / 3) - 4))

    if lvl_start < lvl_end:
        await message.send('{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[f'{user.id}']['level'] = lvl_end

    print(users)
    print('')

async def check_lvl(users, user, message):
    experience = users[f'{user.id}']['experience']
    lvl_end = int(round((20 * experience) ** (1 / 3) - 4))
    await message.send('{} is level {}'.format(user.mention, lvl_end))

#########################################


@bot.command()
async def checklvl(message):
    if message.author != bot.user:
        with open('users.json', 'r') as f:
            users = json.load(f)
        # code
        await check_lvl(users, message.author, message.channel)

        with open('users.json', 'w') as f:
            json.dump(users, f)


@bot.command()
async def ya(ctx):
    await ctx.send('yeet!')


@bot.command()
async def hello(ctx):
    author = str(ctx.author).split('#')
    await ctx.send('Hello ' + author[0])


@bot.command()
async def ZaneBot(ctx):
    await ctx.send('Hai Hai ZaneBot Desu.')


@bot.command()
async def nobully(ctx):
    await ctx.send('plz no bully bot')


@bot.command(brief='this is my brief', help='this is my help', description='this is my test description')
async def test(ctx):
    await ctx.send('pong')


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

    activity = discord.Activity(name="the enemy ", activity=" ", type=discord.ActivityType.watching)
    await bot.change_presence(status=None, activity=activity)


# set type=
# discord.ActivityType.playing
# discord.ActivityType.watching
# no parameters for these ^^


@bot.event
async def on_message(message):
    if message.author != bot.user and '^checklvl' not in message.content:
        with open('users.json', 'r') as f:
            users = json.load(f)
        # code
        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message.channel)

        with open('users.json', 'w') as f:
            json.dump(users, f)

        #######################
    if message.author == bot.user:
        return

    if message.content.startswith('How long did this take?'):
        await message.channel.send('too long')

    if message.content.startswith('What was the cost?'):
        await message.channel.send('Everything...a small price to pay for salvation')

    if message.content.startswith('Ora Ora Ora'):
        await message.channel.send('MUDA MUDA MUDA!')

    if 'tired' in message.content:
        await message.channel.send('<:PandaSleep:478315151934619678>')

    if 'happy' in message.content:
        await message.channel.send('<:PandaDuck:478315152362700808>')

    if 'awesome' in message.content:
        await message.channel.send('<:PandaDuck:478315152362700808>')

    if 'depressed' in message.content:
        await message.channel.send('<:PandaSad:478315151427108902>')

    if 'sad' in message.content:
        await message.channel.send('<:PandaSad:478315151427108902>')

    if 'angry' in message.content:
        await message.channel.send('<:PandaRee:478315151712583681>')

    if message.content.startswith('$greet'):
        await message.channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == message.channel

        msg = await bot.wait_for('message', check=check)
        await message.channel.send('Hello {.author}!'.format(msg))

    await bot.process_commands(message)
    # NEED await bot.process_commands(message) IN ORDER TO USE BOT COMMANDS AT THE END OF ON_MESSAGE


bot.run('NjM1Mjg5MjI3MjY1MDQ4NjA2.XbNpng.0DXPHy8ea1bSI1oHKubsMlI15_s')

# NjM1Mjg5MjI3MjY1MDQ4NjA2.Xa-xnA.pNt2MiAZ2k41PeuMGF0DI6aoAJY
