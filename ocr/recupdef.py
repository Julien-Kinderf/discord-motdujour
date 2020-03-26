from tesserocr import PyTessBaseAPI
import os

os.system('clear')
path_img = "./ocr/img/autoscreens/"
path_txt = "./ocr/txt/temp_txt/"

# Récupération de la liste de tous les screenshots
images = []
for image in os.listdir(path_img):
    images.append(image)


# Lecture des textes des screens
# et mise en forme
texts = []
with PyTessBaseAPI() as api:

    i = 1
    for img in images:
        api.SetImageFile(path_img + img)
        texts.append(api.GetUTF8Text())
        print(f"OCR en cours : {i}/{len(images)}", end="\r")
        i += 1



# On va ensuite tenter de récupérer les deux bouts de la définition
# Insha'Allah on saura les séparer
wordclass = ["verbe", "nom", "adjectif", "adjectit"]
for text in texts:
    text = "\n".join([line for line in text.split("\n") if ((len(line) > 0) and ("Google" not in line) and ("=" not in line) and ("~" not in line) and (line not in wordclass))])

    # Si il y a un 4) dans le texte et qu'il est pas sur la première ligne
    if (("4)" in text) and ("4)" not in text.split()[0])):
        name = text.split("4)")[0]
        text = text.split("4)")[1]

    else: # Soit il y a pas de 4) soit il est sur la prmière ligne
        name = text.splitlines()[0].split(" ")[0]
        text = text.splitlines()[1]

    # Ici dans name on a bien le nom
    # Ici dans text on a tous les paragraphes d'un coup


    with open(path_txt + name, "w") as textfile:
        textfile.write(text)
