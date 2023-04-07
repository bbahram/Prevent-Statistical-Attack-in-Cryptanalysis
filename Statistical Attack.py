import numpy as np
import operator
from numpy.core.defchararray import array, count
from numpy.lib.function_base import append



def DeCrypt(note, array):
    fileWrite=open("./plaintext.txt", "w")

    y=""
    
    for i in note:
        for j in i:
            if j==" ":
                y+=" "
                continue
            elif j=="\n":
                y+="\n"
                continue
            y+=statistics[array.index(j)]


    fileWrite.write(y)
    fileWrite.close()







def StatisticsCallculator():
    global alphabet
    fileRead = open("./cipherText.txt")

    x=fileRead.readlines()
    y=""
    #print(x)
    for i in x:
        for j in i:
            if j!=" " and j!="\n":
                #index=alphabet[0].index(j)
                alphabet[j]+=1

    alphabet = sorted(alphabet.items(), key=operator.itemgetter(1), reverse=True)
    alphabet=dict(alphabet)
    print(alphabet)
    alphabet=list(alphabet)
    
    DeCrypt(x, alphabet)








statistics=["e", "t","a", "o","i", "n","s", "r","h", "d","l", "u","c", "m","f", "y","w", "g","p", "b","v", "k","x", "q","j", "z"]

alphabet={
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}


StatisticsCallculator()

