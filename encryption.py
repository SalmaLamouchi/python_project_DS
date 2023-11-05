
def chiffrement_cesar(mot, decalage):
    mot_chiffre = ""
    for lettre in mot:
        if lettre.isalpha():
            decalage_ascii = 65 if lettre.isupper() else 97
            mot_chiffre += chr((ord(lettre) - decalage_ascii + decalage) % 26 + decalage_ascii)
        else:
            mot_chiffre += lettre
    return mot_chiffre

def dechiffrement_cesar(mot, decalage):
    return chiffrement_cesar(mot, 26 - decalage)

def chiffrement_cesar_26_lettres(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    resultat = ''

    for lettre in message:
        if lettre.isalpha():
            est_majuscule = lettre.isupper()
            lettre = lettre.lower()  
            index = (alphabet.index(lettre) + decalage) % 26
            lettre_chiffree = alphabet[index]
            if est_majuscule:
                lettre_chiffree = lettre_chiffree.upper() 
            resultat += lettre_chiffree
        else:
            resultat += lettre 

    return resultat


def dechiffrement_cesar_26_lettres(mot, decalage):
    return chiffrement_cesar(mot, 26 - decalage)




