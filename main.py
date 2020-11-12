import sys
import mariadb
import discord
import requests
import mariadb
from discord.ext import commands
import json


#Print a Test to Console
print("test")

#Discord Bot initialization + prefix
client = discord.Client()
bot = commands.Bot(command_prefix="!")

#After Bot Startup get the Username + ID
@bot.event
async def on_ready():
    print("Eingeloggt als: " + bot.user.name + str(bot.user.id))

#Check Scammer Command
@bot.command(name="cs", help="Checkt unsere Datenbank, ob der Spieler bekannt ist als Scammer", pass_context=True)
async def check_scammer(ctx, *, message):
        
        #message is the context that gets passed to the request
        
        request = requests.get("https://api.mojang.com/users/profiles/minecraft/%s" % message).json()
        userinput = request.get('id')
        #request return id into variable userinput
        #print userinput for debug
        await ctx.send(userinput)
        
        #establish mariab connection
        try:
            mydb = mariadb.connect(
                host="",
                user="",
                password="",
                database=""
                )
        except mariadb.Error as e:
                print(f"Error connecting to MariaDB Platform: {e}")
                sys.exit(1)

        #just debug
        await ctx.send("test1")

        #SQL Querry 
        mycursor = mydb.cursor()

        sql = ("select * from liste where UUID = '" + userinput +"'")
        mycursor.execute(sql)
        
        #Create list from Querry to easily use the context
        mylist = list(mycursor.fetchall())
        
        #print List for now
        await ctx.send(mylist)



bot.run("")
