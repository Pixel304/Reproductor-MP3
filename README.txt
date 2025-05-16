REPRODUCTOR MP3

Este proyecto como su nombre dice consiste en un reproductor de mùsica creado en Python que obviamente reproduce musica.

En este reproductor puedes:
-cargar tu musica
-reproducir tu musica
-pausar tu musica
-detener tu musica y volverla a escuchar

Puedes usarlo para escuchar musica en tu laptop o computadora mientras estas haciendo alguna otra cosa, como jugar videojuegos, investigando,etc.

Para poder hacerlo, necesitas instalar estos modulos:
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QFileDialog, QLabel
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

Para cargar tu musica al reproductor tienes que correr el programa, luego haz click en el boton "Cargar Mp3" y te abrira tus archivos y por ultimo escoge.
Hay que destacar que necesitas convertir tu musica a mp3
primero copia la IRL de tu musica de un video de youtube y luego ve a este enlace https://v2.youconvert.net/esTekY/ es un convertidor mp3. Pega el IRL y te apareceran 4 botones, haz click en el que dice "Obtener Enlace MP3[128kbps] [S2]" ya descargado haz los pasos para cargar tu musica.

Autor: ChatGPT y Paolo Palacios Rodriguez(pixel304)