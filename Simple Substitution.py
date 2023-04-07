







def EnCrypt():
    global cipherText
    fileRead = open("./plaintext.txt")
    fileWrite=open("./cipherText.txt", "w")

    x=fileRead.readlines()
    y=""
    

    for i in x:
        for j in i:
            if j==" ":
                y+=" "
                continue
            if j=="\n":
                y+="\n"
                continue
            y=y+cipherText[plainText.index(j)]


    fileWrite.write(y)
    fileRead.close()
    fileWrite.close()


def DeCrypt():
    global cipherText
    fileRead = open("./cipherText.txt")
    fileWrite=open("./plaintext.txt", "w")

    x=fileRead.readlines()
    y=""
    
    for i in x:
        for j in i:
            if j==" ":
                y+=" "
                continue
            if j=="\n":
                y+="\n"
                continue
            y=y+plainText[cipherText.index(j)]


    fileWrite.write(y)
    fileRead.close()
    fileWrite.close()





plainText=["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n","o", "p","q", "r","s", "t","u", "v","w", "x","y", "z", " ", "\n"]
cipherText=["z", "y", "x", "w","v", "u","t", "s","r", "q","p", "o","n", "m","l", "k","j", "i","h", "g","f", "e","d", "c","b", "a", " ", "\n"]

n=0
while True:
    n = int(input("1.Enrypt\n2.Decrypt\n"))
    if n>0 and n<3:
        break

if n==1:
    EnCrypt()
else:
    DeCrypt()


