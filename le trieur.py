from pathlib import Path

"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""

files_extensions = { ".mp3": "Musique",
".wav": "Musique",
".flac": "Musique",
".avi": "Videos",
".mp4": "Videos",
".gif": "Videos",
".bmp": "Images",
".png": "Images",
".jpg": "Images",
".docx" : "Documents",
".txt": "Documents",
".pptx": "Documents",
".csv": "Documents",
".xls": "Documents",
".pdf": "Documents",
".odp": "Documents",
".pages": "Documents",
".iso" : "Os",
".zip" : "zip files",
".exe" : "Win prog",
".py" : "Python files"}


BASE_DIR = Path("C:/Users/yaosi/Downloads")


# On récupère tous les fichiers dans le dossier de base
files = [f for f in BASE_DIR.iterdir() if f.is_file()]
for file in files:  # On boucle sur chaque fichier

    #Reccuperation de l'extension de chque fichier
    extension = file.suffix

    #repartir les fichers dans les nouveaux dossiers crées et les autres dans les le dossiers divers
    dossier_cible = files_extensions.get(extension, "Divers")

    #Concatènation du dossier racine et de notre dossier cible
    dossier_cible_absolu = BASE_DIR / dossier_cible

    #Création du dossier et si existant cela ne causerait pas de problème
    dossier_cible_absolu.mkdir(exist_ok=True)

    #association des fichiers selon leur nom dans les dossiers crées
    fichier_cible = dossier_cible_absolu / file.name

    #deplacement des fichiers avec leur nom d'origine
    file.rename(fichier_cible)