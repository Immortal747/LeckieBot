import discord
from discord.ext import commands
from URLReader import URLReader

f = open("token.txt", "r")

PREFIX = '-'

LECKIE_PRE = "http://www.chaoticgolf.com"

LECKIE_URL = "/tutorial_calc_aahs.html"
CHAPTER_URL = "/tutorial_calc_ch#_aahs.html"

ur = URLReader(LECKIE_PRE+LECKIE_URL)

client = commands.Bot(command_prefix = PREFIX)

def begins(text, start):
    return text.content.lower().startswith(PREFIX+start)

def get_vid_num(chapter, section):
    ch_link = ''
    
    if (chapter < 3 or chapter > 6):
        ch_link = CHAPTER_URL.replace('#', str(chapter))

        if ur.find(ch_link)==-1:
            return 'Chapter Not Found!'

    ur.load_new_url(LECKIE_PRE+ch_link)

    ur.print()

    index = ur.find(str(chapter)+'_'+str(section))

    if index==-1:
        return 'Section Not Found!'

    char = ' '
    start = index

    while char!='"' and start>0:
        start-=1
        char = ur.get_text()[start:start+1]

    char = ' '
    end = index

    while char!='"' and end<len(ur.get_text()):
        end+=1
        char = ur.get_text()[end:end+1]

    return LECKIE_PRE+ur.get_text()[start+1:end].replace('.html', '.mp4')

def get_vid_name(name):
    pass
    

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return

    if begins(message, 'ping'):
       await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')

    if begins(message, 'myname'):
        await message.channel.send(f'{message.author.name}')

    if begins(message, 'vid '):

        if len(message.content) < 7:
            await message.channel.send('Give a valid input (i.e. "vid 1-3")')
            return

        text = message.content
        section = text[5:8]
        
        valid = section[0:3:2].isnumeric() and (section[1:2] == '-' or section[1:2] == '.')

        if not(valid):
            await message.channel.send('Send valid section (i.e. 1-3 or 1.3)')
            return

        vid = get_vid_num(int(section[0:1]), int(section[2:3]))
        
        await message.channel.send(vid)

client.run(f.read())
