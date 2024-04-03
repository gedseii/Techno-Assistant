from pytube import YouTube
import os
from youtubesearchpython import VideosSearch
from moviepy.editor import AudioFileClip
import subprocess
def trouver_lien_youtube(mot_cle):
    results = VideosSearch(mot_cle, limit=1)
    videosResult = results.result()
    if results:
        return videosResult["result"][0]['link']
    else:
        return None


def telecharger_audio_youtube(url, dossier_sortie):
    try:
        yt = YouTube(url)
        print(yt.title)
        audio_stream = yt.streams.filter(only_audio=True).first()
        fichier_nom = audio_stream.download(output_path=dossier_sortie)
        return os.path.basename(fichier_nom)  # Récupérer le nom du fichier à partir du chemin complet
    except Exception as e:
        print("Une erreur s'est produite lors du téléchargement :", e)
        return None

def lire_fichier_mp4_avec_vlc(chemin):
    try:
        # Spécifier le chemin complet de l'exécutable VLC
        chemin_vlc = "D:/Application/VLC/vlc.exe"

        # Exécuter VLC avec le chemin du fichier MP4 en argument
        subprocess.Popen([chemin_vlc, chemin])
        print("Lecture du fichier MP4 en cours...")
    except FileNotFoundError:
        print("Erreur: VLC n'est pas installé sur votre système.")



if __name__ == "__main__":
    print("""
·········································································
:████████╗███████╗ ██████╗██╗  ██╗███╗   ██╗ ██████╗                    :
:╚══██╔══╝██╔════╝██╔════╝██║  ██║████╗  ██║██╔═══██╗                   :
:   ██║   █████╗  ██║     ███████║██╔██╗ ██║██║   ██║                   :
:   ██║   ██╔══╝  ██║     ██╔══██║██║╚██╗██║██║   ██║                   :
:   ██║   ███████╗╚██████╗██║  ██║██║ ╚████║╚██████╔╝                   :
:   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝                    :
:                                                                       :
: █████╗ ███████╗███████╗██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗:
:██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝:
:███████║███████╗███████╗██║███████╗   ██║   ███████║██╔██╗ ██║   ██║   :
:██╔══██║╚════██║╚════██║██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║   :
:██║  ██║███████║███████║██║███████║   ██║   ██║  ██║██║ ╚████║   ██║   :
:╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   :
:                                                                       :
·········································································  
    """)
    print(
        """Ce programme vous permet de télécharger l'audio
de la première vidéo YouTube correspondant à votre recherche.
Entrez 'stop' pour quitter à tout moment.
    """)

    while True:
        mot_cle = input("\nEntrez un mot-clé pour rechercher une vidéo sur YouTube : ")
        if mot_cle.lower() == "stop":
            print("\nMerci d'avoir utilisé Techno Assistant. À bientôt !")
            break

        lien_youtube = trouver_lien_youtube(mot_cle)

        if lien_youtube:
            dossier_destination = "D:\Titou\Musique\Techno"
            # Créer le dossier de destination s'il n'existe pas
            if not os.path.exists(dossier_destination):
                os.makedirs(dossier_destination)

            nom_fichier = telecharger_audio_youtube(lien_youtube, dossier_destination)
            if nom_fichier:
                print(f"\nTéléchargement terminé! Le fichier {nom_fichier} a été téléchargé.")
                path = dossier_destination + "/" + nom_fichier
                lire_fichier_mp4_avec_vlc(path)
            else:
                print("\nÉchec du téléchargement de la vidéo.")


        else:
            print("\nAucune vidéo trouvée pour le mot-clé spécifié.")

