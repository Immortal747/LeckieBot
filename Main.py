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
    
    if (chapter < 3 or chapter > 5):
        ch_link = CHAPTER_URL.replace('#', str(chapter))

        if ur.find(ch_link)==-1:
            return 'Chapter Not Found!'

    if (chapter >= 3 or chapter <= 5):
        if chapter==3 and section<=5:
            ch_link = CHAPTER_URL.replace('#', '3')
        if chapter==3 and section>5:
            ch_link = CHAPTER_URL.replace('#', '4')
        if chapter==4 and section<=5:
            ch_link = CHAPTER_URL.replace('#', '4')
        if chapter==4 and section>5:
            ch_link = CHAPTER_URL.replace('#', '5')
        if chapter==5 and section<=5:
            ch_link = CHAPTER_URL.replace('#', '5')

        if ur.find(ch_link)==-1:
            return 'Chapter Not Found!'

    ur.load_new_url(LECKIE_PRE+ch_link)

    index = ur.find('lesson'+str(chapter)+'_'+str(section))

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

    name = name.lower()

    ch_link = ' '
    ch = 0

    while ch<8:
        ch+=1
        ch_link = CHAPTER_URL.replace('#', str(ch))

        ur.load_new_url(LECKIE_PRE+ch_link)

        if ur.get_text().find(name)!=-1:
            char = ' '
            index = ur.find(name)
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

    return 'Video not found!'

def get_vid_name_ch(name, chapter):

    name = name.lower()

    ch_link = ' '
    
    ch_link = CHAPTER_URL.replace('#', str(chapter))

    ur.load_new_url(LECKIE_PRE+ch_link)

    if ur.get_text().find(name)!=-1:
        char = ' '
        index = ur.find(name)
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

    return 'Video not found!'

def get_notes(chapter):

    name = 'worksheets'
    name = name.lower()

    ch_link = CHAPTER_URL.replace('#', str(chapter))

    ur.load_new_url(LECKIE_PRE+ch_link)

    if ur.find(name)!=-1:
        char = ' '
        index = ur.find(name)
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

    return 'Notes not found!'

def get_ws(chapter):

    name = 'worksheets'
    name = name.lower()

    ch_link = CHAPTER_URL.replace('#', str(chapter))

    ur.load_new_url(LECKIE_PRE+ch_link)

    if ur.find(name)!=-1:
        char = ' '
        index = ur.get_text().find(name, ur.get_text().find(name))
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

    return 'Worksheet not found!'

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
    if begins(message, 'you suckv'):
        await message.channel.send(f'Vincent you suck!!')
                                
    if begins(message, 'software'):
        await message.channel.send('Imagine being in software pleb')
    if begins(message, 'quotient'):
        await message.channel.send('Hi dee over hi dee ho ho ho')
    if beings(message, 'conlin'):
        await message.channel.send('YOU HAVE NOTHING AGANIST ME JOHN CONLIN FIGHT ME!!!!!!')
             
              

    if begins(message, 'myname'):
        await message.channel.send(f'{message.author.name}')

    if begins(message, 'shut up'):
        await message.channel.send(f'{message.author.name} I have helped' +
                                   " you all this time. I'm a nice guy." +
                                   " But don't talk to me like that! Hi-De-Ho!")

    if begins(message, 'vid ') and message.content[5:6].isnumeric() and message.content[7:8].isnumeric():

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

    elif begins(message, 'vid '):
        text = message.content
        
        if len(text[5:])<3:
            await message.channel.send('Send valid section')
            return

        ch = ''
        if text[5].isnumeric() and int(text[5])>0 and int(text[5])<8:
            ch=text[5]

        name = ''
        char = '"'
        start = message.content.find(char)
        index = start+1

        char = message.content[index+1: index+2]

        while char!='"':
            index+=1
            char = message.content[index:index+1]

        name = message.content[start+1:index]

        if ch!='':
            vid = get_vid_name_ch(name, int(ch))
        else:
            vid = get_vid_name(name)

        await message.channel.send(vid)

    if begins(message, 'notes '):
        text = message.content

        if not(text[7].isnumeric() and int(text[7])>0 and  int(text[7])<8):
            await message.channel.send('Send valid chapter')
            return

        ch = int(text[7:8])

        notes = get_notes(ch)

        await message.channel.send(notes)

    if begins(message, 'ws '):
        text = message.content

        if not(text[4].isnumeric() and int(text[4])>0 and  int(text[4])<8):
            await message.channel.send('Send valid chapter')
            return

        ch = int(text[4:5])

        ws = get_ws(ch)

        await message.channel.send(ws)

client.run(f.read())
