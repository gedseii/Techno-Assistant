from pytube import YouTube
import os
from youtubesearchpython import VideosSearch

def trouver_lien_youtube(mot_cle):
    results = VideosSearch(mot_cle, limit=1)
    videosResult = results.result()
    if results:
        return videosResult["result"][0]['link']
    else:
        return None

def telecharger_audio_youtube(url, dossier_sortie):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=dossier_sortie)

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
            dossier_destination = "D:/Titou/Musique/Techno"

            # Créer le dossier de destination s'il n'existe pas
            if not os.path.exists(dossier_destination):
                os.makedirs(dossier_destination)

            telecharger_audio_youtube(lien_youtube, dossier_destination)
            print("\nTéléchargement terminé!")
        else:
            print("\nAucune vidéo trouvée pour le mot-clé spécifié.")
