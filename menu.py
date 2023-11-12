import hashlib
from encryption import chiffrement_cesar,dechiffrement_cesar,chiffrement_cesar_26_lettres
from hashage import attaquer_par_dictionnaire
from dataset import afficher_courbes,collecter_dataset,Salaire_AnneeExp,afficher_correlation,analyser_salaires,regression_lineaire,analyser_age,comparer_salaires_par_age,comparer_salaires_par_gender,comparer_salaires_par_experience
import colorama
import maskpass
from art import text2art
s = '*'  
def menu_principal():
    print(colorama.Fore.GREEN)
    print(s*50,"Menu Principal:",s*50)
    print("1- Enregistrement")
    print("2- Authentification")
    print("3- Quitter")


def menu_hashage():
        print(colorama.Fore.GREEN)
        print("a- Haché le mot par SHA-256")
        print("b- Attaquer par dictionnaire  le mot inséré.")
        print("d- Revenir au menu principal")

def menu_cesar_lettre():
        print(colorama.Fore.GREEN)
        print("1- Chiffrer un mot")
        print("2- Déchiffrer un mot")
        
        print("d- Revenir au menu principal")
        sous_choix_cesar = input("Choisissez une option : ")
        print(colorama.Fore.RED)
        if sous_choix_cesar == "1":
                mot = input("Entrez le mot : ")
                decalage = int(input("Entrez la valeur de décalage : "))
                mot_chiffre = chiffrement_cesar_26_lettres(mot, decalage)
                print(f"Mot chiffré par Caesar : {mot_chiffre}")
        elif sous_choix_cesar == "2":
                mot = input("Entrez le mot chiffré : ")
                decalage = int(input("Entrez la valeur de décalage : "))
                mot_dechiffre = dechiffrement_cesar(mot, decalage)
                print(f"Mot déchiffré par Caesar : {mot_dechiffre}")
        
        elif sous_choix_cesar == "d":
                second_menu_after_authentification()
        else:
                print("Option invalide. Choisissez à nouveau.")

def menu_cesar_code_asscii():
        print(colorama.Fore.GREEN)
        print("1- Chiffrer un mot par code ascii")
        print("2- Déchiffrer un mot par code ascii")
        print("3- Revenir au menu principal")
        sous_choix_cesar = input("Choisissez une option : ")
        print(colorama.Fore.RED)
        if sous_choix_cesar == "1":
                mot = input("Entrez le mot : ")
               
                decalage = int(input("Entrez la valeur de décalage : "))
                mot_chiffre = chiffrement_cesar(mot, decalage)
                print(f"Mot chiffré par Caesar : {mot_chiffre}")
        elif sous_choix_cesar == "2":
                mot = input("Entrez le mot chiffré : ")
                decalage = int(input("Entrez la valeur de décalage : "))
                mot_dechiffre = dechiffrement_cesar(mot, decalage)
                print(f"Mot déchiffré par Caesar : {mot_dechiffre}")
        elif sous_choix_cesar == "3":
                second_menu_after_authentification()
        else:
                print("Option invalide. Choisissez à nouveau.")

email=""
def second_menu_after_authentification():
    
   
    while True:
        print(colorama.Fore.GREEN)
        print(text2art("jeux"))
        print("A- Donnez un mot à hacher")
        print("B- Decalage par cesar")
        print("D- Collecter une Dataset de votre choix") 
        print("E- Revenir au menu principale")

        choix = input("Choisissez une option : ")
        print(colorama.Fore.RED)
        if choix == "A":
            mot = maskpass.askpass("Entrez le mot à hasher :")
            print("Vous avez saisi le mot à hacher avec succees !.")
            print(colorama.Fore.GREEN)
            print(s*40,"Options supplémentaires:",s*40)
            menu_hashage()

            sous_choix = input("Choisissez une option : ")

            if sous_choix == "a":
                hashed = hashlib.sha256(mot.encode()).hexdigest()
                print(f"Le mot haché par SHA-256 : {hashed}")
            elif sous_choix == "b":
                attaquer_par_dictionnaire(mot)
            elif sous_choix == "d":
                continue
            else:
                print("Option invalide. Choisissez à nouveau.")
        elif choix == "B":
            print("a-Cesar avec code ASCII")
            print("b-Cesar dans les 26 lettres")
            sous_choix_cesar1 = input("Choisissez une option : ")
            if sous_choix_cesar1=="a":
                menu_cesar_code_asscii()
            elif sous_choix_cesar1=="b":
                menu_cesar_lettre()
                
            
           
        elif choix == "D":
              collecter_dataset_menu()
              
        

        elif choix == "E":
            break

        
def collecter_dataset_menu():
    while True:
        print(colorama.Fore.GREEN)
        print("a- Affichez le Dataset sous forme de dictionnaire")
        print("b- Afficher des courbes")
        print("c- Analyser les salaires")
        print("d- Analyser les ages")
        print("e- Afficher la matrice de corrélation")
        print("f- Effectuer une régression linéaire")
        print("g- Effectuer des comparaisons")
        print("h- Revenir au menu principal")
        choix = input("Choisissez une option : ")
        dataset = collecter_dataset()
        print(colorama.Fore.RED)
        if choix == "a":
            print(dataset)
        elif choix == "b":
            menu_courbe()
        elif choix == "c":
            
            analyser_salaires(dataset)
        elif choix == "d":
            
            analyser_age(dataset)
        elif choix == "e":
            
            afficher_correlation(dataset)
        elif choix == "f":
            
            regression_lineaire(dataset)
        elif choix == "g":
            menu_categorie()
        elif choix == "h":
            second_menu_after_authentification()
        else:
            print("Option invalide. Choisissez à nouveau.")



def menu_courbe():
    while True:
        print(colorama.Fore.RED)
        print("1- Afficher le salaire en fonction du sexe")
        print("2- le salaire en fonction des annees d'experience ")
        print("3- revenir au menu precedent ")
        choix = input("Choisissez une option : ")
        print(colorama.Fore.RED)
        if choix == "1":
            dataset = collecter_dataset()
            afficher_courbes(dataset)
        elif choix == "2":
            dataset = collecter_dataset()
            Salaire_AnneeExp(dataset)
        elif choix=="3":
            collecter_dataset_menu()
       
        else:
            print("Option invalide. Choisissez à nouveau.")


def menu_categorie():
    while True:
        dataset = collecter_dataset()
        print("1-Age")
        print("2-Genre")
        print("3-annee d'experience")
        print("4-Retour ")
        choix = input("Choisissez une option : ")
        if choix == "1":
            
            comparer_salaires_par_age(dataset)
        elif choix == "2":
            comparer_salaires_par_gender(dataset)
            
        elif choix=="3":
            comparer_salaires_par_experience(dataset)
        
        elif choix=="4":
            collecter_dataset_menu()
            


