import discord
from discord.ext import commands
from discord import File
import requests
import json
import aiohttp
import asyncio
import os
client = commands.Bot(command_prefix='>', self_bot=True)
global token
os.system("color 04")
os.system('cls')
print(
f"  _____  _                 _                  \n"
f" |  __ \| |               | |                 \n"
f" | |__) | |__   __ _ _ __ | |_ ___  _ __ ___  \n"
f" |  ___/| '_ \ / _` | '_ \| __/ _ \| '_ ` _ \ \n"
f" | |    | | | | (_| | | | | |_ (_) | | | | | |\n"
f" |_|    |_| |_|\__,_|_| |_|\__\___/|_| |_| |_|\n"
f"                                              \n")

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content.startswith('discord.gift/'):
        mesg = message.content
        url = mesg
        codelis = (mesg.split("/"))
        code = codelis[1]
        print("nitro code:   " + code)
        redeemheaders = {
            'Authorization': token,
            'content-type': 'application/json',
            'payment_source_id': 'null'
        }
        r = requests.post('https://ptb.discordapp.com/api/v6/entitlements/gift-codes/'+ code +'/redeem',headers=redeemheaders)
        e = r.json()
        print("check response:   " + (str(e)))
        return

    elif message.content.startswith('https://discord.gift'):
        mesg = message.content
        url = mesg
        codelis = (mesg.split("/"))
        code = codelis[3]
        print("nitro code:   "+code)
        redeemheaders = {
            'Authorization': token,
            'content-type': 'application/json',
            'payment_source_id': 'null'
        }
        r = requests.post('https://ptb.discordapp.com/api/v6/entitlements/gift-codes/'+ code +'/redeem',headers=redeemheaders)
        e = r.json()
        print("check response:   " + (str(e)))
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("the prefix for the bot is >\n still need help? do >help in a discord channel!")
    print("ctrl + c to stop the script (the script must be running for the self bot to work.).\n\n")


@client.command(name='getroles')
async def roles(ctx, server, spam):
 if server == "current" and spam == "yes":
     server2 = ctx.guild.id
     await spamrolemention(ctx, server2)
 elif server == "current" and spam == "no":
     server2 = ctx.guild.id
     await sendrolemention(ctx, server2)
 elif server != "current" and spam == "yes":
     await spamrolemention(ctx, server)
 elif server != "current" and spam == "no":
     await sendrolemention(ctx, server)


@client.command(name='getemojis')
async def userz(ctx, server):
 if server == "current":
     server2 = ctx.guild.id
     await getemojis(ctx, server2)
 elif server != "current":
     await getemojis(ctx, server)


async def sendrolemention(ctx, server):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
     async with session.get(f"https://canary.discordapp.com/api/v6/guilds/{server}/roles", headers=headers, timeout=10) as r:
      count = 0
      roles = []
      check = "True"
      while check == "True":
        try:
            js = await r.json()
            dict1 = js[count]
            namerole = (dict1['name'])
            roles.append(namerole)
            count += 1

        except:
            check = "False"
            x = (str(roles))
            b = x.replace(",", "\n")
            v = b.replace("'", "")
            y = v.replace("[", "")
            f = y.replace("]", "")
            embed1 = discord.Embed(title='current roles:', description= f , color=discord.Color.from_rgb(255, 0, 0))
            await ctx.send(embed=embed1)
            return


async def spamrolemention(ctx, server):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
     async with session.get(f"https://canary.discordapp.com/api/v8/guilds/{server}/roles", headers=headers, timeout=10) as r:
      count = 0
      roles = []
      check = "True"
      while check == "True":
        try:
            js = await r.json()
            print(js)
            dict1 = js[count]
            namerole = (dict1['id'])
            roles.append(namerole)
            count += 1

        except:
         try:
            check = "False"
            u = (str(roles))
            print(u)
            b = u.replace(', ', '> \n  <@&')
            v = b.replace("'", '')
            y = v.replace('[', '')
            f = y.replace(']', '')
            n = f.replace(f"{ctx.guild.id}>", '@everyone')
            await ctx.send(n)
            return
         except:
                 res_first = n[0:len(n) // 2]
                 res_second = n[len(n) // 2 if len(n) % 2 == 0
                                else ((len(n) // 2)+1):]
                 await ctx.send(res_first)
                 await asyncio.sleep(1)
                 await ctx.send(res_second)
                 return


async def getemojis(ctx, server):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
     async with session.get(f"https://canary.discordapp.com/api/v6/guilds/{server}/emojis", headers=headers, timeout=10) as r:
         v = await r.json()
         print(v)
         count = 0
         p = ctx.author.id
         roles = []
         check = "True"
         while check == "True":
             try:
                 js = await r.json()
                 dict1 = js[count]
                 emojiname = (dict1['name'])
                 emojiid = (dict1['id'])
                 emojianimated = (dict1['animated'])
                 emojigen = (f"{emojianimated} <:{emojiname}:{emojiid}>")
                 roles.append(emojigen)
                 count += 1
             except:
                    check = "False"
                    for i in roles:
                         output = [x for x in roles if 'True' not in x]
                         u = (str(output))
                         b = u.replace(', ', '\n')
                         v = b.replace("'", '')
                         y = v.replace('[', '')
                         f = y.replace(']', '')
                         z = f.replace('False ', '')
                         try:
                             await ctx.send(z)
                             return
                         except:
                            try:
                                res_first = z[0:len(z) // 2]
                                res_second = z[len(z) // 2 if len(z) % 2 == 0
                                               else ((len(z) // 2)+1):]
                                await ctx.send(res_first)
                                await asyncio.sleep(1)
                                await ctx.send(res_second)
                                return
                            except:
                                await ctx.send("likely too many emotes my guy.")
                                return
                        


@client.command(name="dm")
async def dm(ctx, server, *args):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    mesg = ' '.join(args)
    payload = {'recipient_id': server}
    payload2 = {"content": mesg, "tts": False}
    async with aiohttp.ClientSession() as session:
     async with session.post('https://canary.discordapp.com/api/v6/users/@me/channels', headers=headers, json=payload, timeout=10) as src:
        b = await src.json()
        print(b['id'])
        async with session.post(f"https://canary.discordapp.com/api/v6/channels/{b['id']}/messages", headers=headers, json=payload2, timeout=10) as new:
         f = await new.text()
         print(mesg)
         print(f)
         usertest = (client.get_user(int(server)))
         await ctx.send(f"dm has been sent to {usertest}")

@client.command(name="socials")
async def socials(ctx, server):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
     async with session.get(f'https://canary.discordapp.com/api/v6/users/{int(server)}/profile', headers=headers,timeout=10) as src:
        b = await src.json()
        c = b['connected_accounts']
        count = 0
        p = ctx.author.id
        roles = []
        check = "True"
        while check == "True":
            try:
                dict = c[count]
                type = (dict['type'])
                name = (dict['name'])
                id = (dict['id'])
                fin = f"type: {type},account name: {name},account id: {id},"
                roles.append(fin)
                count += 1
            except:
                check = "False"
                for i in roles:
                    output = [x for x in roles if 'True' not in x]
                    u = (str(output))
                    b = u.replace(', ', '\n')
                    v = b.replace("'", '')
                    y = v.replace('[', '')
                    f = y.replace(']', '')
                    z = f.replace(',', '\n')
                    usertest = (client.get_user(int(server)))
                    embed1 = discord.Embed(title=f"socials linked on {usertest}", description=f"```css\n{z}\n```")
                    await ctx.send(embed=embed1)
                    return

client.remove_command('help')

@client.command(name="channel-raid")
async def channel(ctx, num):
    guild = ctx.message.guild
    for i in range(int(num)):
        await guild.create_text_channel("PHANTOM ON TOP")
    await ctx.send("phantom on top")

@client.command(name="nuke")
async def nuke(ctx):
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
        except:
             await ctx.author.message("ez")
    for roles in list(ctx.message.guild.roles):
        try:
            await roles.delete()
        except:
            print("done")

@client.command(name="role-raid")
async def role(ctx, num):
    guild = ctx.message.guild
    var1 = discord.Permissions(0)
    for i in range(int(num)):
        await guild.create_role(name="PHANTOM-ON-TOP", permissions=var1)
    await ctx.send("~~phantom on top~~")

@client.command(name="help")
async def help(ctx):
    embed1 = discord.Embed(title="commands", description="**>channels [channel-id (lists all channels including admin ones you cant see!)]**\n\n**>accountkiller [channelid] [guild-id] [message-id]**\n\n**>getid [mention the user]**\n\n**>dm [user-id] [message contents]**\n\n**>socials [userid]**\n\n**>getemojis [server-id]**\n\n**>getroles [serverid or just put current] [yes/no for mass mention]**\n\n**>ascii [message you want to make art!]**\n\n**>channel-raid [number of channels to make!]**\n\n**>nuke [deletes ALL channels!]**\n\n**>role-raid [num of roles to make]**\n\n**>socials [user-id (checks linked socials)]**\n\n**this bot also acts as a nitro sniper.**")
    embed1.set_footer(text="this bot was made by phantom\nphantom#3862")
    await ctx.send(embed=embed1)


@client.command(name="accountkiller")
async def accountkiller(ctx, arg1, arg2, arg3):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    payload = {
        'channel_id': arg1,
        'guild_id': arg2,
        'message_id': arg3,
        'reason': "Harassment"}
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://discord.com/api/v6/report', headers=headers, json=payload) as src:
         b = await src.text()
         await ctx.send(b)

@client.command(name="getid")
async def getid(ctx, member : discord.Member):
    embed1 = discord.Embed(title=f"userid for {member}", description=f"```py\n{member.id}\n```")
    await ctx.send(embed=embed1)

@client.command(name="massreport")
async def massreport(ctx, arg1, arg2):
    usertest = (client.get_user(int(arg1)))
    await ctx.send(f"user: {usertest} has been mass reported with {arg2} reports, using server: OVH2")


@client.command(name='ascii')
async def ascii(ctx, *, art: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://artii.herokuapp.com/make?text={art}") as r:
         text = await r.text()
         await ctx.send('```\n' + text + '```\n')


@client.command(name='channels')
async def channels(ctx, arg1):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
     async with session.get(f"https://canary.discordapp.com/api/v6/guilds/{arg1}/channels", headers=headers, timeout=10) as r:
         z = await r.text()
         print(z)
         count = 0
         names = []
         check = "True"
         while check == "True":
             try:
                 z = await r.json()
                 dict1 = z[count]
                 channelname = (dict1["name"])
                 names.append(channelname)
                 count += 1
             except:
                 check = "False"
                 for i in names:
                     output = [x for x in names if 'True' not in x]
                     u = (str(output))
                     b = u.replace(', ', '\n')
                     v = b.replace("'", '')
                     y = v.replace('[', '')
                     f = y.replace(']', '')
                     z = f.replace('False ', '')
                 else:
                     try:
                         embed1 = discord.Embed(title="following channels found:", description=z)
                         await ctx.send(embed=embed1)
                         return
                     except:
                         try:
                             res_first = z[0:len(z) // 2]
                             res_second = z[len(z) // 2 if len(z) % 2 == 0
                                            else ((len(z) // 2)+1):]
                             embed1 = discord.Embed(title="following channels found:", description=res_first)
                             embed2 = discord.Embed(title="following channels found:", description=res_second)
                             await ctx.send(embed=embed1)
                             await asyncio.sleep(1)
                             await ctx.send(embed=embed2)
                             return
                         except:
                             await ctx.send("error")


@client.command(name='banned')
async def banned(ctx, arg1):
    if arg1 == "current":
        b = ctx.guild.id
        await bannedreal(ctx, b)
    else:
        await bannedreal(ctx, arg1)

async def bannedreal(ctx, arg1):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
     async with session.get(f"https://canary.discordapp.com/api/v6//guilds/{arg1}/bans", headers=headers, timeout=10) as r:
         z = await r.text()
         count = 0
         names = []
         check = "True"
         while check == "True":
             try:
                 z = await r.json()
                 dict1 = z[count]
                 print(dict1)
                 dict2 = dict1['user']
                 usernamef = (dict2['username'])
                 tag = (dict2['discriminator'])
                 fullusr = f"{usernamef}#{tag}"
                 names.append(fullusr)
                 count += 1
             except:
                 check = "False"
                 for i in names:
                     output = [x for x in names if 'True' not in x]
                     u = (str(output))
                     b = u.replace(', ', '\n')
                     v = b.replace("'", '')
                     y = v.replace('[', '')
                     f = y.replace(']', '')
                     z = f.replace('False ', '')
                 else:
                     try:
                         print(z)
                         embed1 = discord.Embed(title=f"banned users: {len(names)}", description=z)
                         await ctx.send(embed=embed1)
                         return
                     except:
                         try:
                             res_first = z[0:len(z) // 2]
                             res_second = z[len(z) // 2 if len(z) % 2 == 0
                                            else ((len(z) // 2)+1):]
                             embed1 = discord.Embed(title=f"banned users: {len(names)}", description=res_first)
                             embed2 = discord.Embed(title=f"more:", description=res_second)
                             try:
                                 await ctx.send(embed=embed1)
                                 await asyncio.sleep(1)
                                 await ctx.send(embed=embed2)
                                 return
                             except:
                                 await ctx.send("error maybe too many users to list or none?")
                         except:
                             await ctx.send("error maybe too many users to list or none?")






def login():
 try:
   global token
   print("dont know how to get your token? watch this!: https://www.youtube.com/watch?v=YEgFvgg7ZPI")
   token = input("insert your token: ")
   os.system('cls')
   os.system('color 02')
   client.run(token, bot=False)
 except:
     os.system('cls')
     os.system('color 04')
     print("invalid token, try again.")
     login()

login()


