import hashlib


def hacher_sha256(mot):
    hashed = hashlib.sha256(mot.encode()).hexdigest()
    return hashed

def attaquer_par_dictionnaire(mot):
    mot_hache = hacher_sha256(mot)

    with open('dictionnaire.txt', 'r') as fichier:
        dictionnaire = [hacher_sha256(m) for m in fichier.read().splitlines()]
    if mot_hache in dictionnaire:
        print(f"Le mot original de ce hashage '{mot_hache}' est '{mot}'. L'attaque a réussi.")
    else:
        print("Le mot haché n'a pas été trouvé dans le dictionnaire. L'attaque a échoué.")