from menu import menu_principal,second_menu_after_authentification
from authentification import verifier_authentification,enregistrer,introduire_email,introduire_password


while True:
    menu_principal()
    choix = input("Choisissez une option : ")

    if choix == "1":
        email = introduire_email()
        pwd = introduire_password()
        if enregistrer(email, pwd):
            print("Enregistrement réussi.Merci de s'authentifier !")
        else:
            print("L'enregistrement a échoué.")
        

    elif choix == "2":
        s = '*'
        email = introduire_email()
        pwd = introduire_password()
        if verifier_authentification(email, pwd):
            print("Authentification réussie.")
            print(s*50,f"Bienvenu {email.split('@')[0]}!",s*50)
            second_menu_after_authentification()

        else:
            print("Authentification échouée. Veuillez vous enregistrer.")

    elif choix == "3":
        print("au revoir :) ")
        break

    else:
        print("Option invalide. Choisissez à nouveau.")