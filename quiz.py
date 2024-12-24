import random
import os
from colorama import Fore, Style, init

# Initialisation de colorama pour activer les codes ANSI
init(autoreset=True)

def afficher_menu():
    print(Fore.CYAN + "\n--- MENU ---" + Style.RESET_ALL)
    print("1. Démarrer le quiz")
    print("2. Quitter")

def poser_question(question, options, reponse):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + "\n" + question + Style.RESET_ALL)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choix = int(input(Fore.BLUE + "Tu choisi quoi?: " + Style.RESET_ALL))
            if 1 <= choix <= len(options):
                return choix == reponse
            else:
                print(Fore.RED + "Met un numéro valide..." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Met un numéro valide..." + Style.RESET_ALL)

def demarrer_quiz():
    questions = [
        ("Quel composant est considéré comme le cerveau d'un ordinateur?", ["Carte mère", "CPU", "GPU", "RAM"], 2),
        ("Quel type de stockage est le plus rapide?", ["Disque dur", "SSD", "CD-ROM", "Clé USB"], 2),
        ("Quelle est la fonction principale d'un GPU?", ["Calculer les graphiques", "Stocker des données", "Gérer la mémoire", "Alimenter l'ordinateur"], 1),
        ("Quelle connectique est utilisée pour les cartes graphiques modernes?", ["AGP", "PCIe", "ISA", "SATA"], 2),
        ("Quelle est la principale fonction de la RAM?", ["Stocker des données à long terme", "Gérer les processus actifs", "Rendre les graphismes plus nets", "Alimenter le CPU"], 2),
        ("Quel élément maintient le processeur à une température stable?", ["Ventilateur", "Radiateur", "Pâte thermique", "Tous les choix précédents"], 4),
        ("Quel composant est responsable de l'affichage sur l'écran?", ["Carte mère", "Carte graphique", "Alimentation", "SSD"], 2),
        ("Quelle marque est connue pour ses processeurs Ryzen?", ["Intel", "AMD", "NVIDIA", "ARM"], 2),
        ("Quelle unité mesure la fréquence d'un processeur?", ["MHz", "GHz", "RPM", "kW"], 2),
        ("Quel type de mémoire est intégré au processeur pour stocker temporairement des données?", ["SSD", "RAM", "Cache", "ROM"], 3),
        ("Quelle est la fonction principale de l'alimentation (PSU)?", ["Distribuer l'énergie électrique", "Gérer les données", "Refroidir le système", "Améliorer les graphismes"], 1),
        ("Quel connecteur est principalement utilisé pour les disques durs internes modernes?", ["IDE", "SATA", "USB", "PCIe"], 2),
        ("Quelle est la durée de vie moyenne d'un SSD par rapport à un disque dur?", ["Plus courte", "Similaire", "Plus longue", "Dépend du fabricant"], 3),
        ("Quelle technologie est utilisée pour les écrans tactiles modernes?", ["LCD", "LED", "Capacitifs", "Plasma"], 3),
        ("Quel est le rôle principal d'une carte mère?", ["Gérer les graphismes", "Connecter tous les composants", "Stocker des données", "Fournir de l'énergie"], 2),
        ("Quel est l'avantage principal d'un refroidissement liquide par rapport à l'air?", ["Moins de bruit", "Coût réduit", "Installation facile", "Durée de vie plus longue"], 1),
        ("Quelle norme de RAM est la plus rapide?", ["DDR3", "DDR4", "DDR5", "DDR2"], 3),
        ("Quel périphérique est essentiel pour entrer des données dans l'ordinateur?", ["Moniteur", "Clavier", "Carte réseau", "RAM"], 2),
        ("Quel composant est utilisé pour connecter un PC à Internet?", ["Carte graphique", "Carte réseau", "Alimentation", "Carte son"], 2)
    ]

    random.shuffle(questions)
    erreurs = 0
    
    print(Fore.GREEN + "\nBienvenue sur le quiz! Tu a droit a 3 erreurs" + Style.RESET_ALL)

    for i, (question, options, reponse) in enumerate(questions[:20], 1):
        print(Fore.MAGENTA + f"\nQuestion {i}/{len(questions[:20])}:" + Style.RESET_ALL)
        if not poser_question(question, options, reponse):
            erreurs += 1
            print(Fore.RED + "Mauvaise réponse!" + Style.RESET_ALL)
            if erreurs >= 3:
                print(Fore.RED + "\nTu a atteint la limite d'erreurs. Fin du quiz!" + Style.RESET_ALL)
                return
        else:
            print(Fore.GREEN + "Bonne réponse!" + Style.RESET_ALL)

    print(Fore.CYAN + "\nFélicitations! Tu as terminé le quiz." + Style.RESET_ALL)

def main():
    while True:
        afficher_menu()
        choix = input(Fore.BLUE + "\nChoisi une option... " + Style.RESET_ALL)
        if choix == "1":
            demarrer_quiz()
        elif choix == "2":
            print(Fore.CYAN + "\nMerci d'avoir joué!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Option invalide..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
