
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import datetime
import csv


TOKEN = 'MTE1MzY1NDk2MjQ5NzI2OTgxMQ.GNnPjK.iRQYCcaQGywe-wxOIcW9NAnocJdEfFn58lCC2k'  



bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())


def fetchlivescore():
    try:
        current_time = datetime.datetime.now()


        url='https://www.espncricinfo.com/live-cricket-score'



        response=requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        status=soup.find_all(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')[0].text
        t1=soup.find_all(class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')[0].text
        s1=soup.find_all(class_='ds-text-typo-mid3')[0].text
        k=s1.split(',')
        overt1=k[0]
        t2=soup.find_all(class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')[1].text
        overt2=soup.find_all(class_='ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap')[1].text
        matchdate=soup.find_all(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3')[1].text
        date=soup.find_all(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3')[1].text
        a=matchdate.split(',')
        date=""
        date=date+a[2]+" "+a[3]
        livescoredata="Fetching the live score ...\n" \
                        f" {t1} vs {t2}\n" \
                        f" {status}\n" \
                        f" {t1}:{overt1} \n "\
                        f" {t2}:{overt2}\n" \
                        f" {matchdate}\n" \
                        f" Date {date}"
        with open("liveScore1.csv","a+") as file:
            writer=csv.writer(file)
            print(type(livescoredata))
            x=livescoredata
            x+=f" ., {current_time} "
            l=[]
            l.append(x)
            writer.writerow(l)

        return(livescoredata)
        
    
    except:
        return("Failed to fetch livescore/No live event right now...")





@bot.event
async def on_ready():
    print(f'{bot.user.name} is now online.')
@bot.command()
async def hello(ctx):
    await ctx.send('Hey There!,Howdy!!')
@bot.command()
async def help1(ctx):
    await ctx.send('!livescore :Gives live cricket scores! \n !help1: All commands i cand do :)\n !hello : I Can say hello too!! \n !generate : All data you fetched about cricket events!!')
@bot.command()
async def livescore(ctx):
    x=fetchlivescore()
    await ctx.send(x)
@bot.command()
async def generate(ctx):
    f=discord.File('liveScore1.csv')
    await ctx.send(file=f)


bot.run(TOKEN)



