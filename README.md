# Hacksu-Lesson-Discord-Bot-Advanced
## Intro
Discord, for those who are unfamilar, is a free text and voice chatting platform. You will need a Discord account in order to make and interact with a bot. You can create an account free at their [website](https://discord.com). You can either use Discord through the Desktop Application or through the browser. Additionally, you will need Python 3.8 installed. You can download Python from [here](https://python.org)
## Installing discord.py
In order to be able to code your bot, you will need to install the Discord.py module. To do so, follow these steps.

1: Open up your computer's command line interface. For Windows, this is a program called Command Prompt (or Powershell if you would prefer). For Mac and Linux, this is called Terminal. 
2: Execute the following command
```
pip install discord
```
If Python was installed correctly, you should see output that looks somewhat like (yours will probably look slightly different) to this:
![pip successful](https://i.imgur.com/fQpGOzT.png)
If you don't see this and/or you get an error stating "pip is not recognized as a command" then you will need to unistall and then reinstall Python. When you reinstall, make SURE that you check the box that says "Add Python to your PATH". If you do not, you will not be able to use the pip command to get Discord.py.
## Creating a Server
Now that you are able to make a bot, you need to make a place for it to live. To get started, open up Discord and follow these steps:

1: Select the plus button at the bottom of your server list.

![add a server](https://i.imgur.com/xpYb4bU.png)

2: Select the "Create My Own" button.

![create my own](https://i.imgur.com/0j2pswe.png)

3: Name the server whatever you want, and then click "Create"

![name server](https://i.imgur.com/OdIlEhC.png)

You should now see a blank server in your server list!

![blank server](https://i.imgur.com/YBfzuF5.png)

## Now to create the bot
Last step before coding; we have to tell Discord to make the bot account for us. Go to the [Discord Developer Portal](https://discordapp.com/developers/applications) and follow these steps:

1: Select "New Application", and name your bot whatever you would like.

2: When the application is created, go to the "Bot" tab and select "Add Bot" and then "Yes, do it!"

3: Click on the "Copy" button that appears. This will copy the bot's Token to your clipboard, which is essentially the bot's username and password. Do not share this token with anyone else. 

## Adding the bot to the server
Navigate back to your bot's Application page and follow these steps:

1: Go to the OAuth2 tab

2: From the checklist, select "bot"

3: Copy the URL it gives you, and paste it into your browser

4: From the list of servers, select the server you want to add the bot to, and then click "Authorize". If prompted, solve a CAPTCHA.

You should now see the bot in the member list, but it will say it is offline. To make it appear online, we have to actually code the bot's logic!
## Coding the bot
Now to write the bot. This lesson recommends using Python IDLE (which comes with your installation of Python) to code, but any IDE will work.

Create a new folder where you want your code to be, and then inside that folder create a new file called "bot.py".

The first step is to add the include statements. We need 4 modules in order to code our bot. Add these to your file:
```
import discord
import asyncio
from datetime import *
import random
```
```discord``` is the module we just downloaded with pip. The other modules are things we need to create our bot.

The next step is to create a class that inherits from the discord.Client class. Creating an inherited class allows us to make our own personal bot by adding our own features. Don't worry if you don't know exactly what an inherited class means, it isn't neccessary to creating your bot.
Type ```class MyClient(discord.Client):``` to your file, and then hit enter. Make sure your cursor is also tabbed over after you hit enter.

This class is where we are going to add all of our bot's functionality. First, we need to have the bot awaken and perform actions when it sees that someone has sent a message. To do this, we will create a function called ```on_message```.

Add this inside your class
```
async def on_message(self,message):
    if(message.content.startswith("/")):
        await self.process_commands(message)
```

The ```on_message``` function is a function we have overloaded from the base ```discord.Client``` class. This function will be called every time the bot sees a message from a user. We then check if the message begins with our command key (which can be changed from a slash to be whatever you want), and calls the ```process_commands``` function, which we will make next.

The ```process_commands``` function is where the bot figures out what command the user called - if any. At the end of this, we are going to have 4 different commands, but for right now we are just adding one command, ```/ping```.
```
async def process_commands(self,message):
    command = message.content.split()[0].lower()
    #Command List Here
    if(command == "/ping"):
        await self.pong(message)
```
As you can see, we first split the message the user sent and the extract the first word - which should be the /command the user tried to call. We check if it equals our command ```/ping```, and if it is, we call the ping command.

The ```/ping``` command is relatively simple - all it will do is respond with ```pong```. The code for this function is:
```
async def pong(self,message):
    await message.channel.send("pong")
```
When this function is called, the bot finds the channel that the original message was sent in, and responds with a message that says "pong"

I'm sure you've noticed the ```await``` and ```async``` that appears everywhere. The ```async``` keyword allows us to define a function that can be run asynchronously - i.e., it can run while other asynchronous commands are being run. This lets our bot do many different things at once, and helps speed up response time. The ```await``` keyword must be used when calling a asynchronous function.

We now have a bot that can actually do something - so lets get it running. Go to the bottom of your code and add these 4 lines:
```
bot = MyClient()
file = open("TOKEN.txt",'r')
TOKEN = file.read()
bot.run(TOKEN)
```
These lines of code take your bot's unqiue token out of a .txt file, and connect to Discord's servers using the token. This is a similar process to you logging into Discord using your email and password. We need to create the ```TOKEN.txt``` file that our code is referring to however, so go back to the folder you made and add this file. Open it up, and paste the token you copied from your bot's application page.

Right now, your bot should like the following:
```
import discord
import asyncio
from datetime import *
import random

class MyClient(discord.Client):    

    async def on_message(self,message):
        if(message.content.startswith("/")):
            await self.process_commands(message)

    async def process_commands(self,message):
        command = message.content.split()[0].lower()
        #Command List Here
        if(command == "/ping"):
            await self.pong(message)

    async def pong(self,message):
        await message.channel.send("pong")
        
bot = MyClient()
file = open("TOKEN.txt",'r')
TOKEN = file.read()
bot.run(TOKEN)
```

If you have done everything right, you should have a fully functioning bot! Run the bot, go to the server, and type ```/ping``` to see if it responds!
## The Final Commands
As of now, your bot can only do one thing - say ```pong``` whenever someone says ```/ping```. Bots can do so much more though. To demonstrate, we are going to make our bot manage our server, and then also play a game!
### Server Management
If a bot is made an administrator of a server, it can do things like ban people, create channels, change nicknames, etc. Let's make a command that will create text and voice channels for us.

Return to the ```process_commands``` function and add this below the if statement:
```
elif(command == "/create_channel"):
    await self.create_channel(message)
```
Now our bot will call this function whenever a user types ```/create_channel```. Define the function as follows:
```
async def create_channel(self,message):
```
The first part of this function is going to be some checks we do to make sure that our bot is able to make the channel in the first place. Add the following logic to the function:
```
command = message.content.split()
if(len(command) <= 2):
    await message.channel.send("Invalid usage.")
elif(not message.channel.permissions_for(message.author).manage_channels):
    await message.channel.send("You don't have permission to use this command")
elif(not message.channel.permissions_for(message.guild.me).manage_channels):
    await message.channel.send("I do not have permission to create a channel")
```
The first line of this breaks the message's content into a list of strings. Then, in the if statement, we check if there are 2 or less strings in that list. If there are, this means that the user has not typed enough, and we don't have enough info to create the channel. We send a warning error and then continue.

The two elifs check that the user calling the command and the bot itself has permission from the server to create the channel. We don't want just anyone to be able to create a channel, and if the bot doesn't have permission to create the channel, it wouldn't be able to do it.

Lastly, add this to the function:
```
else:
    if(command[1] == "text"):
        await message.guild.create_text_channel("-".join(command[2:]))
    elif(command[1] == "voice"):
        await message.guild.create_voice_channel(" ".join(command[2:]))
    else:
        await message.channel.send("Invalid usage")
```
If the command the user sent went through all the above checks, we can try to make the channel. In this else statement, we have a nested if-elif-else. If the 2nd word of the command was "text", we create a text channel. If it was "voice", we create a voice channel. If it wasn't either, we send an error message. Run your bot again, and try out the command. If the bot tells you that it doesn't have permission, give it a role with the administrator option checked.
### Guessing Game
We will now make a command that starts a back-and-forth dialoge between a user and your bot in order to play a game! The game is going to be the simple 1-100 number guessing game, but you can be as creative as you want!
To start, add the command to ```process_commands```:
```
elif(command == "/guessing"):
    await self.guessing_game(message)
```
And then add the function declaration:
```async def guessing_game(self,message):```
This function is going to be more complicated than the others, so the code will be shown, and then an explaination for it will be given.

```
def check(m):
    return m.author == message.author
```
In Python, you can declare a function within a function that can only be used in that scope. This function takes another message, and returns if its author is the same author as the original message. It will be used later.
```
guesses = 0
secret = random.randint(1,100)
playing = True
mention = message.author.mention
channel = message.channel
await channel.send("Let's play a guessing game, "+mention+"! I'm thinking of a number between 1 and 100.")
```
This just creates a few values we need, and then sends a game start message.
```
while(playing):
    await channel.send("You have made "+str(guesses)+ " guess"+("es " if guesses != 1 else " ")+mention+"! What is your next guess?")
    try:
        msg = await self.wait_for("message",check=check,timeout = 10)
    except asyncio.TimeoutError:
        await channel.send("You took too long to respond "+mention+". Game Over.")
        return
```
We start a while loop that will run until we change ```playing``` to be false. We then send a message to the user that asks them to send a number. We then start a ```wait_for```. ```wait_for``` is a powerful function that lets us tell our current process to stop and wait for a certain action to be run. In our case here, this action is ```on_message```. You can do other things though, like ```on_reaction_add``` and many more. We give the ```wait_for``` a fuction called ```check``` that returns true when the author of the message matches the author of the original command call. Finally, we specify a timeout period. If the timeout period expires, we stop the game. If we get a response before then, we continue onto:
```
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
```
In this part of the code, we first try to convert what the user entered into an integer. If it fails and errors, we report the error and start the loop over. Otherwise, we continute and check if the user's guess was correct. If it was, we set ```playing``` to false and print a winning message. Otherwise, we tell the user whether the secret number is higher or lower, and then continue.
```
await channel.send("It took you "+str(guesses)+" to find the number. Congrats "+mention)
```
This is the last line of our game, and it just tells the user how many tries it took them to win.
### Help and Extras
Our last command is a help function. This is a function that will explain the other functions to other users, so they now how to use them. Add this last code to ```process_commands```:
```
elif(command == "/help"):
    await self.help(message)
```
And then this function:
```
async def help(self,message):
    await message.channel.send("""Here are all of my commands:```
/help - shows this message
/ping - pong!
/create_channel <text|voice> <channel name> - creates a voice or text channel
/guessing - play a guessing game with the bot
```""")
```
This help function is no more complex than the ```/ping``` function; all it does it print out the instructions for each command.

Finally, the ```on_message``` function is only one of many overloadable functions that are run when the bot encounters something. We are going to overload two more for this bot, but know that there are tons more to use.

The first is ```on_connect```:
```
async def on_connect(self):
    print("Bot has connected to server at time:",datetime.now())
```
```on_connect``` is called whenever the bot connects to Discord's servers through the Internet. Here, we just have the bot print a message and a time stamp.

The second is ```on_ready```:
```
async def on_ready(self):
    await self.change_presence(activity=discord.Game(name = "/help"))
    print("Successfully set Bot's game status")
```
```on_ready``` is called whenever the bot is first launched and becomes ready to run commands. Here, we tell the bot to set its Discord presence to be "Playing a game: /help". Doing this shows users what the help command is, so they can figure out all the things it can do.

## Unique Challenge
Our bot is finally done, but that doesn't mean we have exhausted everything it can do! Bots are limitless with what they can do, and you can do basically anything you want with them! As this week's Unique Bingo Challenge, read through the official Discord.py documentation (found [here](https://discordpy.readthedocs.io/en/latest/api.html)), and implement a feature that wasn't used in this lesson! This can be something like posting an image, giving itself a nickname, anything you want! Show a leader your bot in action and the new code you made, and you can check off that unique feature section on your Bingo Card!
