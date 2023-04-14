#!/usr/bin/env python3

import os
import sys
import glob
import eyed3

ruta = sys.argv

try:
    if os.path.isdir(ruta[1]):   # confirmamos si la ruta pasada por parametros es un directorio valido
        busqueda = ruta[1] + "/*.mp3"
        for mp3 in glob.glob(busqueda):   # pasamos a glob la busqueda de archivos que queremos y los iteramos uno a uno
            audiofile = eyed3.load(mp3)   # con el modulo eye3d cargamos los metadatos del archivo mp3 en audiofile
            if audiofile.tag.title == None or audiofile.tag.artist == None:
                print("{} no dispone de metadatos".format(mp3))
            else:
                print("{} de {}.".format(audiofile.tag.title,audiofile.tag.artist))
    else:
        print("Ruta Incorrecta!!")
except IndexError:
    print("Faltan parametros!!")