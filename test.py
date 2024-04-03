import subprocess


def lire_fichier_mp4_avec_vlc(chemin):
    try:
        # Spécifier le chemin complet de l'exécutable VLC
        chemin_vlc = "D:/Application/VLC/vlc.exe"

        # Exécuter VLC avec le chemin du fichier MP4 en argument
        subprocess.Popen([chemin_vlc, chemin])
        print("Lecture du fichier MP4 en cours...")
    except FileNotFoundError:
        print("Erreur: VLC n'est pas installé sur votre système.")


# Exemple d'utilisation de la fonction
chemin_fichier_mp4 = 'D:\Titou\Musique\Techno\Ivy.mp4'
lire_fichier_mp4_avec_vlc(chemin_fichier_mp4)
