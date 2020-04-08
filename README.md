# discord_motdujour

## This is a very simple discord server made for fun.

### The mot du jour functionnality
The bot reacts to the command *=mot* and sends back an interesting french word and it's definition. 
The words are in the txt/words directory. They have been recuperated on a mobile word of the day app using the homemade *recupscreens.sh* that took more than 1000 screenshots of the app, then processed with the *recupdef.py* script that used the tesseract api on the screenshots.
For this functionnality, the server just chooses a random word and displays it properly for the user.

### The di/cri functionnaly
This functionnality is implemented directly in the discord bot and consists in detecting when someone uses the sound "cri" or "di" in a sentence, and answer to it. This is just a lame french joke. Don't do this.