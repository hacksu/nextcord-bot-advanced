import discord
import asyncio
from datetime import *
import random


class MyClient(discord.Client):

    
    #ON MESSAGE
    async def on_message(self,message):
        if(message.content.startswith("/")):
            await self.process_commands(message)



    #PROCESS COMMANDS
    async def process_commands(self,message):
        command = message.content.split()[0].lower()
        #Command List Here
        if(command == "/ping"):
            await self.pong(message)
        elif(command == "/create_channel"):
            await self.create_channel(message)
        elif(command == "/guessing"):
            await self.guessing_game(message)
        elif(command == "/help"):
            await self.help(message)


    async def pong(self,message):
        await message.channel.send("pong")


    async def create_channel(self,message):
        command = message.content.split()
        if(len(command) <= 2):
            await message.channel.send("Invalid usage.")
        elif(not message.channel.permissions_for(message.author).manage_channels):
            await message.channel.send("You don't have permission to use this command")
        elif(not message.channel.permissions_for(message.guild.me).manage_channels):
            await message.channel.send("I do not have permission to create a channel")
        else:
            if(command[1] == "text"):
                await message.guild.create_text_channel("-".join(command[2:]))
            elif(command[1] == "voice"):
                await message.guild.create_voice_channel(" ".join(command[2:]))
            else:
                await message.channel.send("Invalid usage")

    async def guessing_game(self,message):
        def check(m):
            return m.author == message.author
        guesses = 0
        secret = random.randint(1,100)
        playing = True
        mention = message.author.mention
        channel = message.channel
        await channel.send("Let's play a guessing game, "+mention+"! I'm thinking of a number between 1 and 100.")
        while(playing):
            await channel.send("You have made "+str(guesses)+ " guess"+("es " if guesses != 1 else " ")+mention+"! What is your next guess?")
            try:
                msg = await self.wait_for("message",check=check,timeout = 10)
            except asyncio.TimeoutError:
                await channel.send("You took too long to respond "+mention+". Game Over.")
                return
            else:
                try:
                    num = int(msg.content)
                    guesses += 1
                    if(num == secret):
                        playing = False
                        await channel.send("Good job! You got the number "+mention)
                    else:
                        await channel.send("The secret number is "+("higher " if num < secret else "lower ")+mention)
                except:
                    guesses -= 1
                    await channel.send("You need to send me a valid integer.")
        await channel.send("It took you "+str(guesses)+" to find the number. Congrats "+mention)     
        
    async def help(self,message):
        await message.channel.send("""Here are all of my commands:```
/help - shows this message
/create_channel <text|voice> <channel name> - creates a voice or text channel
/guessing - play a guessing game with the bot
```""")

    #WHEN READY
    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name = "/help"))
        print("Successfully set Bot's game status")


    #CONNECTION
    async def on_connect(self):
        print("Bot has connected to server at time:",datetime.now())



print("Starting Bot")
bot = MyClient()
file = open("TOKEN.txt",'r')
TOKEN = file.read()
#print(TOKEN)
bot.run(TOKEN)
