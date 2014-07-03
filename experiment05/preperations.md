# Preperations V6 FaceRecognition

## Was sind Eigenvektoren und Eigenwerte?
Ein Eigenvektor ist ein normalisierter Vektor, dessen Faktor durch den Eigenwert bestimmt wird und sich bei einer Abbildung nicht verändert.

sind orthgonal paaarweise 

## Was versteht man unter Eigenfaces?
Eigenfaces sind die relevanten Merkmale eines Bildes

Im Fall der Gesichtserkennung werden die relevanten Merkmale auch als Eigenfaces bezeichnet.
Jedes Eigenface kann als Bild dargestellt werden, welches ein bestimmtes Gesichtsmerkmal besonders hervorhebt. Jedes individuelle Bild der Kategorie (d.h. jedes Gesicht) kann dann als Linearkombination der K relevanten Merkmale (der K Eigenfaces) beschrieben werden.



## Die PCA ist u.a. im entsprechenden Kapitel des Dokuments [PCAJM] beschrieben. Wie kann mit
der PCA eine Dimensionalitätsreduktion durchgeführt werden?

In einem NxM  dimensionalen Raum sind alle Bilder beschrieben. Um ähnliche Bilder zu beschrieben braucht man aber nicht so viele Dimensionen, da die Varianz innehalb einzelner Dimensionen sehr gering sein wird, haben die Dimensionen keine Aussagekraft über die Bilder.


## Wie werden mit dem Python Modul Image Bilder in ein Python-Programm geladen?

from PIL import Image

im = Image.open("cat.jpg") # laden des Bildes aus dem aktuellen Verzeichnis
im.show() # anzeigen des Bildes