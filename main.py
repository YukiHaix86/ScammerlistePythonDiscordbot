import sys
import mariadb
import discord
import requests
import mariadb
from discord.ext import commands
import json

# Print a Test to Console
print("test")

# Discord Bot initialization + prefix
client = discord.Client()
bot = commands.Bot(command_prefix="!")


# After Bot Startup get the Username + ID
@bot.event
async def on_ready():
    print("Eingeloggt als: " + bot.user.name + str(bot.user.id))


# Check Scammer Command
@bot.command(name="cs", help="Checkt unsere Datenbank, ob der Spieler bekannt ist als Scammer", pass_context=True)
async def check_scammer(ctx, *, message):
    # message is the context that gets passed to the request

    request = requests.get("https://api.mojang.com/users/profiles/minecraft/%s" % message).json()
    userinput = request.get('id')
    # request return id into variable userinput
    # print userinput for debug
    #await ctx.send(userinput)

    # establish mariab connection
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

    # just debug
   # await ctx.send("test1")

    # SQL Query
    mycursor = mydb.cursor()

    sql = ("select * from liste where uuid = '" + userinput + "' order by datum desc limit 1")
    mycursor.execute(sql)

    # Create list from Query to easily use the context
    mylist = list(mycursor.fetchall())

    OutputString = str(mylist).strip('[]')

    OutputList = OutputString.split(',')

    print(OutputList[2].strip("'").strip(" '"))

    request = requests.get("https://api.mojang.com/users/profiles/minecraft/%s" % message).json()
    username = request.get('name')

    embedOut = discord.Embed(title="FCR-Scammerliste Suche", description="Wir haben unsere Datenbank dursucht", color=0x00ff00)
    embedOut.set_thumbnail(url="https://minotar.net/cube/"+userinput+"/400.png")
    embedOut.add_field(name="Spielername", value=username, inline=False)
    embedOut.add_field(name="Datenbank ID", value=OutputList[0].strip("'").strip(" '").strip(" ("), inline=True)
    embedOut.add_field(name="UUID", value=userinput, inline=False)
    embedOut.add_field(name="Hinterlegter Beweis", value=OutputList[3].strip("'").strip(" '"), inline=False)

    await ctx.send(embed=embedOut)

bot.run("")
