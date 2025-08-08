import os
import shutil

from datetime import datetime

Annee = datetime.now().year
Mois = datetime.now().month

# Demande à l'utilisateur de saisir le nom du projet

Saisi = input("Saisissez le nom du projet : ")
Dir = os.path.join("D:\\# Mes Pellicules photo\\")

# Création du dossier de destination.
destination_dir = str(Dir) + str(Annee)[-2:] + " 0" + str(Mois) + " " + str(Saisi)
os.mkdir(destination_dir)


# Dossier de départ (à changer selon vos besoins)
start_dir = "E:\\"

# Liste pour stocker tous les chemins complets trouvés
all_files = []

# Liste temporaire de dossiers à scanner (initialement contient seulement le dossier de départ)
dirs_to_scan = [start_dir]


while dirs_to_scan:
    current_dir = dirs_to_scan.pop()
    # Liste tous les éléments dans le dossier courant
    for item in os.listdir(current_dir):
        path = os.path.join(current_dir, item)
        if os.path.isdir(path):
            # Si c'est un dossier, on l'ajoute à la liste à scanner
            dirs_to_scan.append(path)
        else:
            # Si c'est un fichier, on l'ajoute à la liste des fichiers trouvés
            all_files.append(path)
            # Vérifie si le fichier se termine par ".CR3" (insensible à la casse)
            if item.lower().endswith('.cr3'):
              # Copie le fichier vers le dossier de destination
              shutil.copy2(path, destination_dir)
              

# Affichage de tous les fichiers trouvés
for file_path in all_files:
    print(file_path)


print("Transfert terminé !")