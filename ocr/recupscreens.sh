#!/usr/bin/env bash

NBIMAGES=1089
echo "Récupération de $NBIMAGES images de mots du jour"


for ((i = 0 ; i < $NBIMAGES ; i++)); do
    # Capture de l'écran
    sleep 1
    adb shell screencap /storage/self/primary/autoscreens/image_$i.png
    echo -en "$i écrans scannés\r"

    # Swipe pour passer à l'écran suivant
    adb shell input swipe 200 950 900 950 150
done


# Récupération des images
echo "Rapatriement des images"
adb pull /storage/self/primary/autoscreens/ ./img/


echo "Fait"