#generator to make the text file
def generator():
    outfile=open("Original.txt","w")
    for i in range (5):
        line=input('insert your line:')
        outfile.write(line+'\n')
    outfile.close()

def Encrypt(file,shifts):
    if shifts>26:
        shifts=shifts%26
    Encrypted=""
    infile=open(file,"r")
    for line in infile:
        for character in line:
            if character.isalpha():
                if character.isupper():
                    if (ord(character)+shifts>90):
                        enccharacter=chr(ord(character)-26+shifts)
                        Encrypted+= enccharacter
                    else:
                        enccharacter=chr(ord(character)+shifts)
                        Encrypted+= enccharacter
                else:
                    if (ord(character)+shifts>122):
                        enccharacter=chr(ord(character)-26+shifts)
                        Encrypted+= enccharacter
                    else:
                        enccharacter=chr(ord(character)+shifts)
                        Encrypted+= enccharacter
            else:
                enccharacter=character
                Encrypted+= enccharacter
    infile.close()
    outfile=open(r"Ciphered.txt","w")
    outfile.write(Encrypted)
    outfile.close()

def Decrypt(file,shifts):
    if shifts>26:
        shifts=shifts&26
    Encrypted=""
    infile=open(file,"r")
    for line in infile:
        for character in line:
            if character.isalpha():
                if character.isupper():
                    if (ord(character)-shifts)<65:
                        enccharacter=chr(ord(character)+26-shifts)
                        Encrypted+= enccharacter
                    else:
                        enccharacter=chr(ord(character)-shifts)
                        Encrypted+= enccharacter
                else:
                    if (ord(character)-shifts<97):
                        enccharacter=chr(ord(character)+26-shifts)
                        Encrypted+= enccharacter
                    else:
                        enccharacter=chr(ord(character)-shifts)
                        Encrypted+= enccharacter
            else:
                enccharacter=character
                Encrypted+= enccharacter
    infile.close()
    outfile=open(r"Deciphered.txt","w")
    outfile.write(Encrypted)

generator()
Encrypt(r"Original.txt",1)
Decrypt(r"Ciphered.txt",1)


