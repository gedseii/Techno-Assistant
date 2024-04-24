import sys
from tqdm import tqdm
from pytube import YouTube
import os
from youtubesearchpython import VideosSearch
from moviepy.editor import AudioFileClip
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyOAuth

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

def lancer_playlist_vlc():
    dossier = r'D:\Titou\Musique\Techno'
    fichiers = [fichier for fichier in os.listdir(dossier) if fichier.endswith('.mp4')]
    chemins = [os.path.join(dossier, fichier) for fichier in fichiers]
    print(chemins)
    chemin_vlc = "D:/Application/VLC/vlc.exe"
    subprocess.Popen([chemin_vlc] + chemins)

def extract_playlist_name(playlist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='30015381e44a46e4bb6413b970e3accb',
                                                   client_secret='30c02160e4b844188b67269a2ee67c31',
                                                   redirect_uri='http://localhost:8080/callback',
                                                   scope='playlist-read-private'))
    playlist = sp.playlist(playlist_id)
    name = []
    artists = []
    for track in playlist['tracks']['items']:
        name.append(track['track']['name'])
        artists = ', '.join([artist['name'] for artist in track['track']['artists']])

    resultat = []
    for piste, artiste in zip(name, artists):
        resultat.append(f"{piste} - {artiste}")
    return resultat

def create_links(playlist_songs):
    liens = []
    print("Extraction des urls Youtube")
    with tqdm(total=len(playlist_songs)) as pbar:
        for song in playlist_songs:
            lien = trouver_lien_youtube(song)
            liens.append(lien)
            pbar.update(1)
        return liens
def telecharger_playlist(liste_songs_urls,dossier_sortie):
    print("Téléchargement de la playlist")
    with tqdm(total=len(liste_songs_urls)) as pbar:
        for url in liste_songs_urls:
            telecharger_audio_youtube(url,dossier_sortie)
            pbar.update(1)

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
Ou bien de télécharger une playlist à partir d'un url de playlist spotify.
Entrez 'stop' pour quitter à tout moment.
    """)

    #mot_cle = input("\nEntrez un URL de playlist Spotify : ")
    playlist_id = input("\nEntrez l'id d'une playlist Spotify pour télécharger les sons : ")
    songs = extract_playlist_name(playlist_id)
    liens = create_links(songs)
    dossier_destination = "D:\Titou\Musique\Techno"
    telecharger_playlist(liens, dossier_destination)
    input()

    while True:
        mot_cle = input("\nEntrez un mot-clé pour rechercher une musique sur YouTube : ")
        if mot_cle.lower() == "stop":
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

    mot_cle = input("\n Lancer la playlist - Entrer 'Y' : ")
    while True:
        mot_cle = input("\n (Re)Lancer la playlist - Entrer 'y' : ")
        if mot_cle == 'y':
            lancer_playlist_vlc()
        else:
            print("\nMerci d'avoir utilisé Techno Assistant. À bientôt !")
            sys.exit()
