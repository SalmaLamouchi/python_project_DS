import hashlib
import re
import maskpass

def introduire_password():
    import string
    global pwd

    while True:
        try:
            pwd = maskpass.askpass()
            
            if len(pwd) != 8:
                raise ValueError("Le mot de passe doit avoir une longueur de 8 caractères.")
            if not any(t in string.digits for t in pwd):
                raise ValueError("Le mot de passe doit contenir au moins un chiffre.")
            if not any(t in string.ascii_uppercase for t in pwd):
                raise ValueError("Le mot de passe doit contenir au moins une lettre majuscule.")
            if not any(t in string.ascii_lowercase for t in pwd):
                raise ValueError("Le mot de passe doit contenir au moins une lettre minuscule.")
            if not any(t in string.punctuation for t in pwd):
                raise ValueError("Le mot de passe doit contenir au moins un caractère spécial.")

            pwd = hashlib.sha256(pwd.encode()).hexdigest()
            return pwd

        except ValueError as error:
            print("Erreur:", error)



def introduire_email():
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    while True:
        global email  
        email = input("Donnez votre email :")
        if re.fullmatch(regex, email):
            return email
        else:
            print('Email invalide, merci d\'entrer un email sous format (exemple@gmail.com)')

def verifier_authentification(email, pwd):
    with open('Enregistrement.txt', 'r') as fichier:
        for ligne in fichier:
            info = ligne.strip().split(', ')
            if info[0].split(': ')[1] == email and info[1].split(': ')[1] == pwd:
                return True
    return False

def enregistrer(email, pwd):
    with open('Enregistrement.txt', 'r') as fichier:
        for ligne in fichier:
            info = ligne.strip().split(', ')
            if info[0].split(': ')[1] == email:
                print("Erreur: Cet e-mail est déjà enregistré.")
                return False  

    if not email or not pwd:
        print("Erreur: L'e-mail et le mot de passe doivent être renseignés.")
        return False

    try:
        with open('Enregistrement.txt', 'a') as fichier:
            fichier.write(f'Email: {email}, Pwd: {pwd}\n')
        return True
    except Exception as e:
        print("Erreur lors de l'enregistrement :", e)
        return False

