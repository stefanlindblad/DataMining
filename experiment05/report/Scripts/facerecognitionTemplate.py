from os.path import isdir,join,normpath
from os import listdir

from PIL import Image
from numpy import asfarray,dot,argmin,zeros, array, asarray
from numpy import average,sort,trace,copy
from numpy.linalg import svd,eigh,norm
from numpy import concatenate, reshape
from math import sqrt
import sys

import tkFileDialog
from patsy.util import wide_dtype_for

NUMFEATURES = 4


def parseDirectory(directoryName,extension):
    '''This method returns a list of all filenames in the Directory directoryName. 
    For each file the complete absolute path is given in a normalized manner (with 
    double backslashes). Moreover only files with the specified extension are returned in 
    the list.
    '''
    if not isdir(directoryName): return
    imagefilenameslist=sorted([
        normpath(join(directoryName, fname))
        for fname in listdir(directoryName)
        if fname.lower().endswith('.'+extension)            
        ])
    return imagefilenameslist

#####################################################################################
# Implement required functions here
#
#
#

def generateListOfImgs(listOfTrainFiles):
    imgList = []
    for trainFile in listOfTrainFiles:
        imgList.append(Image.open(trainFile))
    return imgList

def convertImgListToNumpyData(imgList):
    imgArrays = []
    for img in imgList:
        imgArray = asfarray(img).reshape((1, -1))[0]
        max = imgArray.max()
        imgArray /= max
        imgArrays.append(imgArray)

    return asarray(imgArrays)

def calculateAverageImg(images):
    return average(images, axis=0)

def removeAverageImage(images, avgImage):
    for image in images:
        image -= avgImage
    return images

def calculateEigenfaces(faces, width, height):
    M = len(faces)
    w, v = eigh(faces.T.dot(faces))
    u = faces.dot(v)
    index = w.argsort()[::-1]
    w=w[index]
    u=u[:, index]
    return u

def transformToEigenfaceSpace(eigenfaces, face, numFeatures):
    pointToEigenspace = zeros(shape=(numFeatures))
    for i in range(numFeatures):
        pointToEigenspace[i] = dot((eigenfaces[:,i:i+1].T), face)
    return pointToEigenspace



####################################################################################
#Start of main programm

#Choose Directory which contains all training images 
TrainDir=tkFileDialog.askdirectory(title="Choose Directory of training images")
#Choose the file extension of the image files
Extension='png'

images = convertImgListToNumpyData(generateListOfImgs(parseDirectory(TrainDir, Extension)))


avgImage = calculateAverageImg(copy(images))
normedArrayOfFaces = removeAverageImage(copy(images), avgImage)

Image.fromarray(avgImage.reshape((220, 150))*250).show()

eigenfaces = calculateEigenfaces(normedArrayOfFaces.T, len(images[0]), len(images))
transposedFaces = []
for face in normedArrayOfFaces:
    transposedFaces.append(transformToEigenfaceSpace(eigenfaces, face, NUMFEATURES))


#Image.fromarray(avgImage.reshape((220, 150))*250).show()

#Choose the image which shall be recognized
testImageDirAndFilename=tkFileDialog.askopenfilename(title="Choose Image to detect")

testImage = Image.open(testImageDirAndFilename)
testface = convertImgListToNumpyData([testImage])[0]
testface -= avgImage
Image.fromarray(testface.reshape((220, 150))*250).show()

testface = transformToEigenfaceSpace(eigenfaces, testface, NUMFEATURES)

distance = sys.float_info.max
closestMatchIndex = 0
for index, face in enumerate(transposedFaces):
    newdistance = norm(testface - face)
    if distance > newdistance:
        closestMatchIndex = index
        distance = newdistance

Image.fromarray(images[closestMatchIndex].reshape((220, 150))*250).show()
testImage.show()

####################################################################################
# Implement required functionality of the main programm here


