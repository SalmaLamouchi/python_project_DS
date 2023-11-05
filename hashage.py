import hashlib


def hacher_sha256(mot):
    hashed = hashlib.sha256(mot.encode()).hexdigest()
    return hashed

def attaquer_par_dictionnaire(mot):
  
    with open('dictionnaire.txt', 'r') as fichier:
        dictionnaire = fichier.read().splitlines()
        hacher_sha256(mot)
    if mot in dictionnaire:
        print(f"Le mot original de ce hashage '{hacher_sha256(mot)}'est '{mot}'. L'attaque a réussi.")
        
    else:
        print(f"Le mot haché  n'a pas été trouvé . L'attaque a échoué.")