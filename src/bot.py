import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

# Global variables
pathToCurrentDirectory = os.path.realpath(__file__)
pathToWords = os.path.dirname(pathToCurrentDirectory) + "/../ocr/txt/words"
pathToUsedWords = os.path.dirname(
    pathToCurrentDirectory) + "/../ocr/txt/used_words"


def getword():
    # This function returns a list containing :
    # - the word of the day
    # - it's defintion
    # - the examples

    # let's choose a random word among all of our words
    word = random.choice(os.listdir(pathToWords))
    #print(f"Le mot choisi est : {word}")

    # let's get the textfile associated with this word
    with open(pathToWords + '/' + word, 'r') as textfile:
        word_text = textfile.read()

    # let's format it nicely for discord
    word_text = word_text.replace("\n", " ").replace(
        ".", ".\n").strip().replace("\n ", "\n")
    #print(f"Sa définition est la suivante : \n{word_text}\n")

    # let's move the file to the used words folder
    #os.replace(pathToWords + '/' + word, pathToUsedWords + '/' + word)
    #print(f"==> Mot {word} déplacé dans 'used_words/'")

    result = [word, word_text]
    return(result)


def backToDefault():
    # This function is useful only in developpment phase
    # It transfers back all of the files from used_words to words
    for word in os.listdir(pathToUsedWords):
        os.replace(pathToUsedWords + '/' + word, pathToWords + '/' + word)


os.system('clear')
# backToDefault()

# First get the word of the day
wordOfTheDay = getword()

# Then connect to discord
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='=', description="test")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    activity = discord.Activity(
        name='Confinement Simulator 2020', type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)


@bot.event
async def on_message(message):
    if message.author != bot.user:  # On vérifie que le bot ne se répond pas à lui même
        reponse = ""
        # GESTTION DU DI
        if ("di" in message.content.lower()):
            i = message.content.lower().index("di")
            reponse = message.content[i + 2:].strip()

            if(len(reponse) > 2):
                # On regarde si c'était un di simple ou pas
                if (reponse.lower()[0] in "stx" and reponse.lower()[1] == ' '):
                    reponse = reponse[2:].strip()

            if (len(reponse) > 0):
                # Envoi de la réponse finale
                print(
                    f"Sending {reponse} because {message.author} said \"di\"""")
                await message.channel.send(reponse)

        # GESTTION DU CRI
        if ("cri" in message.content.lower()):
            i = message.content.lower().index("cri")
            reponse = message.content[i + 3:].upper().strip()

            if (len(reponse) > 2):
                # On regarde si c'était un cri simple ou pas
                if (reponse[0:2].lower() == "e "):
                    reponse = reponse[2:].strip()

            # Ajout des points d'exclamation parce qu'il s'agit de bien crier
            reponse += " !!!"

            if (len(reponse) > 0):
                # Envoi de la réponse finale
                print(
                    f"Sending {reponse} because {message.author} said \"di\"""")
                await message.channel.send(reponse)

        # GESTION DU COIFFEUR
        quois = ["quoi", "quoi ?", "quoi?"]
        if (message.content.lower() in quois):
            reponse = "Feur !"

            # Envoi de la réponse
            print(
                f"Sending {reponse} because {message.author} deserved it")
            await message.channel.send(reponse)
    # Si le message est une commande, elle sera gérée par cette méthode
    await bot.process_commands(message)


@bot.command()
async def quitter(ctx):
    """Leaves the server."""
    print(f"Closing the bot as asked by {ctx.author.name}")
    await bot.close()


@bot.command()
async def mot(ctx):
    """Send a random word and it's definition"""
    word = getword()
    #print(f"Le mot trouvé est :\n{word}")

    definition = word[1].replace(".\n", '.\n\n*', 1) + '*'
    word = word[0]

    message = f"__**{word} :**__\n{definition}\n"
    await ctx.send(message)
    print(f"Word asked by {ctx.author.name} : {word} delivered")


bot.run(token)
