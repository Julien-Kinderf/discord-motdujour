import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

# Global variables
pathToWords = os.path.dirname(__file__) + "/../ocr/txt/words"
pathToUsedWords = os.path.dirname(__file__) + "/../ocr/txt/used_words"

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
    word_text = word_text.replace("\n", " ").replace(".", ".\n").strip().replace("\n ", "\n")
    #print(f"Sa définition est la suivante : \n{word_text}\n")

    # let's move the file to the used words folder
    os.replace(pathToWords + '/' + word, pathToUsedWords + '/' + word)
    #print(f"==> Mot {word} déplacé dans 'used_words/'")


    result = [word, word_text]
    return(result)

def backToDefault():
    # This function is useful only in developpment phase
    # It transfers back all of the files from used_words to words
    for word in os.listdir(pathToUsedWords):
        os.replace(pathToUsedWords + '/' + word, pathToWords + '/' + word)



os.system('clear')
backToDefault()

# First get the word of the day
wordOfTheDay = getword()

# Then connect to discord
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
print(token)

bot = commands.Bot(command_prefix='?', description="test")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    await bot.close()




bot.run('token')