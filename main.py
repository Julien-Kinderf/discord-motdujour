# bot.py
import os
import asyncio
import discord
import random
from dotenv import load_dotenv

os.system('clear')
path_words = "./ocr/txt/temp_txt/"
mots = os.listdir(path_words)
mot = random.choice(mots)

with open(path_words + mot, "r") as textfile:
    definition = textfile.read()

message = f"Salut, je suis le bot Mot du Jour ! Le mot du jour est : {mot}\n\n{mot} :{definition}"
#print(message)

#Connexion au serveur discord et envoi du message
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
@client.event
async def on_ready():
    print(f"{client.user} s'est bien connecté à discord !")
    
    for channel in client.get_all_channels():
        if "mot-du-jour" == channel.name:
            print("Je suis ici")
            await channel.send(content=message)



    await client.close()

@client.event
async def on_disconnect():
    print("Deconnexion")


client.run(TOKEN)